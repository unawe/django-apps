# from datetime import datetime
import uuid
import os
import re

from django.db import models
# from django.conf import settings
# from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
# from django.contrib.admin.models import LogEntry
# from django.contrib.contenttypes.models import ContentType
from parler.models import TranslatableModel, TranslatedFieldsModel
from parler.managers import TranslatableManager, TranslatableQuerySet
#from taggit.managers import TaggableManager
# from taggit.models import TagBase, GenericTaggedItemBase
from taggit_autosuggest.managers import TaggableManager
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from autoslug import AutoSlugField

from django_ext.models import PublishingModel, PublishingManager, MediaAttachedModel, BaseAttachmentModel
from glossary.models import Entry as GlossaryEntry
from . import tasks

# Space Scoop app settings
# Default translation credits
DEFAULT_TRANSLATION_CREDITS = {
    'en': {'text': '', 'url': ''},
    'nl': {'text': 'Vertaling door Marieke Baan/NOVA', 'url': 'http://www.astronomie.nl'},
    'is': {'text': 'Þýðing: Sævar Helgi Bragason/Stjörnufræðivefurinn', 'url': 'http://www.stjornufraedi.is'},
    'id': {'text': 'Diterjemahkan oleh langitselatan', 'url': 'http://www.langitselatan.com'},
    'it': {'text': 'Traduzione di Lucia Morganti/UNAWE', 'url': 'http://it.unawe.org'},
    'mt': {'text': 'Maqlub għall-Malti minn Alexei Pace', 'url': 'http://www.maltastro.org'},
    'pl': {'text': 'Tłumaczenie: ', 'url': 'http://www.astronomia.pl'},
    'pt': {'text': '', 'url': 'http://www.portaldoastronomo.org'},
    'ro': {'text': 'Traducere: Cătălina Movileanu/UNAWE', 'url': 'http://www.unawe.ro'},
    'es': {'text': 'Traducciones de Amelia Ortiz-Gil/Observatorio Astronomico-Universidad de Valencia, y Breezy Ocaña/', 'url': 'http://observatori.uv.es/'},
    'tr': {'text': 'Çeviri: Arif Solmaz / Çağ Üniversitesi Uzay Gözlem ve Araştırma Merkezi, Mersin', 'url': 'http://arifsolmaz.wordpress.com/uzay-gazetesi/'},
    'uk': {'text': 'Переклад від Зої Малої', 'url': 'http://space-scoop.blogspot.com/'},
    'si': {'text': 'Universe Awareness Sri Lanka', 'url': 'http://unawe-srilanka.blogspot.com'},
    'vi': {'text': 'VietAstro biên dịch / Translated by VietAstro', 'url': 'http://www.vietastro.org'},
}

SPACEAWE_CATEGORY_CHOICES = (
    ('space', 'Our wonderful Universe'),
    ('planet', 'Our fragile planet'),
    ('nav', 'Navigation through the ages'),
    ('herit', 'Islamic heritage'),
)


class Category(TranslatableModel):
    position = models.IntegerField(default=0, )

    #TODO: cache result
    def code(self):
        return self.get_translation('en').slug

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('categories:detail', kwargs={'slug': self.slug, })

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('position', )


class CategoryTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Category, related_name='translations', null=True)
    slug = AutoSlugField(max_length=200, populate_from='title', always_update=True, unique_with=('language_code',))
    # slug = models.SlugField(max_length=200, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')
    title = models.CharField(_('title'), max_length=200)

    class Meta:
        unique_together = (
            ('language_code', 'master'),
            ('language_code', 'slug'),
        )


class OriginalNewsSource(TranslatableModel):
    name = models.CharField(max_length=200, unique=True, help_text='Short (and commonly used) name', )
    slug = models.SlugField(max_length=200, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', )
    fullname = models.CharField(max_length=200, blank=True, help_text='If set, the full name will be used in some places instead of the name', )
    url = models.CharField(max_length=255)
    logo = ImageField(null=True, blank=True, upload_to='partners')
    article_count = models.IntegerField(default=0, editable=False, )

    def title(self):
        return self.fullname if self.fullname else self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('partners:detail', kwargs={'slug': self.slug, })

    class Meta:
        verbose_name = 'partner'


class OriginalNewsSourceTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(OriginalNewsSource, related_name='translations', null=True)
    description = RichTextField(blank=True, null=True, config_name='small', help_text='Text to appear in Parnet page')
    # more_about = RichTextField(blank=True, null=True, config_name='small', help_text='Text to appear after the "learn more about this partner" links')

    class Meta:
        unique_together = (
            ('language_code', 'master'),
        )
        verbose_name = 'partner translation'


class ArticleQuerySet(TranslatableQuerySet):
    pass


class ArticleManager(PublishingManager, TranslatableManager):
    queryset_class = ArticleQuerySet


# class LowerCaseTag(TagBase):
#     def save(self, *args, **kwargs):
#         self.name = self.name.lower()
#         super().save(*args, **kwargs)

# class LowerCaseTaggedItem(GenericTaggedItemBase):
#     tag = models.ForeignKey(LowerCaseTag, related_name="tagged_items")


class Article(TranslatableModel, PublishingModel, MediaAttachedModel):

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=4, blank=False, db_index=True, help_text='The 4 digit code that identifies the Article, in the format "YY##": year, folowed by sequential number.')
    categories = models.ManyToManyField(Category, related_name='articles', limit_choices_to={'translations__language_code': 'en'})
    spaceawe_category = models.CharField(max_length=20, blank=True, choices=SPACEAWE_CATEGORY_CHOICES, )
    original_news = models.ManyToManyField(OriginalNewsSource, through='OriginalNews', related_name='articles', )

    objects = ArticleManager()
    # tags = TaggableManager(blank=True, through=LowerCaseTaggedItem)
    tags = TaggableManager(blank=True)
    # available = PublishingManager()

    @property
    def translated_credit(self):
        result = ''
        if self.translation_credit_text and self.translation_credit_url:
            result = u'<a href="%s">%s</a>' % (self.translation_credit_url, self.translation_credit_text)
        elif self.translation_credit_text:
            result = self.translation_credit_text
        elif self.translation_credit_url:
            result = '<a href="%s">%s</a>' % (self.translation_credit_url, self.translation_credit_url)
        return result

    # def get_absolute_url_full(self):
    #     return utils.get_qualified_url(self.get_absolute_url())

    # def download_url(self, resource):
    #     return os.path.join(settings.MEDIA_URL, self.media_key(), 'download', self.download_key() + '.' + resource)
    # def download_path(self, resource):
    #     return os.path.join(settings.MEDIA_ROOT, self.media_key(), 'download', self.download_key() + '.' + resource)

    def story_expanded(self):
        result = self.story
        for entry in self._get_glossary_entries()[0]:
            search_text = r'<glossary slug="%s">(.*?)</glossary>' % entry.slug
            replace_text = '<a class="glossary" href="/glossary/%s" title="%s">\\1</a>' % (entry.slug, entry.short_description, )
            result = re.sub(search_text, replace_text, result)
        return result
        # return re.sub(r'<glossary slug="(.*?)">(.*?)</glossary>', '<a class="glossary" href="/glossary/\\1" title="Hooray!">\\2</a>', self.story)

    #TODO: cache the result
    def _get_glossary_entries(self):
        present = []
        missing = []
        for slug in re.findall(r'<glossary slug="(.*?)">.*?</glossary>', self.story):
            entries = GlossaryEntry.objects.filter(
                # translations__language_code__in=get_active_language_choices(),
                translations__language_code=self.language_code,
                translations__slug=slug
            )
            if entries:
                present.append(entries[0])
            else:
                missing.append(slug)
        return (present, missing)

    # #TODO: cache the result
    # def _get_glossary_entries(self):
    #     present = []
    #     missing = []
    #     for code in re.findall(r'<glossary code="(.*?)">.*?</glossary>', self.story):
    #         entries = GlossaryEntry.objects.filter(code=code)
    #         if entries:
    #             present.append(entries[0])
    #         else:
    #             missing.append(code)
    #     return (present, missing)

    def get_glossary_entries(self):
        return self._get_glossary_entries()[0]

    def get_glossary_entries_missing(self):
        return self._get_glossary_entries()[1]

    def is_translation_fallback(self):
        return not self.has_translation(self.language_code)

    @classmethod
    def add_prefetch_related(self, qs, prefix=""):
        # add _after_ qs.filter! see django docs on prefetch_related
        if prefix:
            prefix += '__'
        qs = qs.prefetch_related('%stranslations' % prefix)
        qs = qs.prefetch_related('%scategories' % prefix)
        qs = qs.prefetch_related('%scategories__translations' % prefix)
        qs = qs.prefetch_related('%simages' % prefix)
        return qs

    def __str__(self):
        return self.code + ': ' + self.title

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'code': self.code, 'slug': self.slug, })

    class Meta(PublishingModel.Meta):
        pass

    # class PublishingMeta(PublishingModel.PublishingMeta):
    #     permission_all = publishing_login_required()
    #     permission_embargoed = publishing_login_required()


# @receiver(post_save, sender=Article)
# def article_post_save(sender, instance, created, **kwargs):
#     tasks.populate_article_count()


class ArticleTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Article, related_name='translations', null=True)
    slug = AutoSlugField(max_length=200, populate_from='title', always_update=True, unique=False)
    # slug = models.SlugField(max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')
    title = models.CharField(_('title'), max_length=200)
    # lead = RichTextField(blank=True, config_name='small')
    story = RichTextField(config_name='spacescoop')
    cool_fact = RichTextField(blank=True, null=True, config_name='small')
    translation_credit_text = models.CharField(max_length=255, blank=True, null=True, help_text='If set, this text will replace the default translation for credits.')
    translation_credit_url = models.CharField(max_length=255, blank=True, null=True, )
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = (
            ('language_code', 'master'),
            # ('language_code', 'slug'),
        )


def get_file_path_article_attachment(instance, filename):
    return os.path.join('articles/attach', str(instance.hostmodel.uuid), filename)


# class Attachment(BaseAttachmentModel):
#     hostmodel = models.ForeignKey(Article)
#     file = models.FileField(blank=True, upload_to=get_file_path_article_attachment)


class Image(BaseAttachmentModel):
    hostmodel = models.ForeignKey(Article, related_name='images')
    file = ImageField(null=True, blank=True, upload_to=get_file_path_article_attachment)
    # main_visual = models.BooleanField(default=False, help_text=_(u'The main visual is used as the cover image.'))


class OriginalNews(models.Model):
    article = models.ForeignKey(Article)
    original_news_source = models.ForeignKey(OriginalNewsSource)
    url = models.CharField(max_length=255, verbose_name='URL')

    class Meta:
        verbose_name_plural = 'original news'

    def __str__(self):
        return self.url


#TODO maybe it is more efficient to run this as a daily task (it goes through all articles anyway)?
@receiver(post_save, sender=OriginalNews)
def originalnews_post_save(sender, instance, created, **kwargs):
    tasks.populate_article_count()
