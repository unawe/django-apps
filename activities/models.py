import uuid
import os
import re

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse
# from django.contrib.redirects.models import Redirect
# from django.contrib.sites.models import Site
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
# from tinymce.models import HTMLField
# from markupfield.fields import MarkupField
# from markupmirror.fields import MarkupMirrorField
from parler.models import TranslatableModel, TranslatedFieldsModel
from parler.managers import TranslatableManager, TranslatableQuerySet
from autoslug import AutoSlugField
from sorl.thumbnail import ImageField

from django_ext.models import PublishingModel, PublishingManager
from django_ext.models.spaceawe import SpaceaweModel
from . import utils, tasks
# # from filemanager.models import File as ManagedFile
from institutions.models import Institution, Person

# # def get_file_path(instance, filename):
#     return os.path.join('activities/attach', instance.uuid, filename)


def get_file_path_step(instance, filename):
    return os.path.join('activities/attach', str(instance.hostmodel.uuid), filename)


ACTIVITY_SECTIONS = (
    ('description', 'Brief Description'),
    ('goals', 'Goals'),
    ('objectives', 'Learning Objectives'),
    ('evaluation', 'Evaluation'),
    ('materials', 'Materials'),
    ('background', 'Background Information'),
    ('fulldesc', 'Full Activity Description'),
    ('curriculum', 'Curriculum'),
    ('additional_information', 'Additional Information'),
    ('conclusion', 'Conclusion'),
)

ACTIVITY_METADATA = (
    ('age', 'Age',
        {'display': 'age_range', }),
    ('level', 'Level',
        {'multiple': True, }),
    ('time', 'Time',
        {'display': 'time', }),
    ('group', 'Group',
        {'display': 'group', }),
    ('supervised', 'Supervised',
        {'display': 'supervised', }),
    ('cost', 'Cost',
        {'display': 'cost', }),
    ('location', 'Location',
        {'display': 'location', }),
    ('skills', 'Core skills',
        {'multiple': True, }),
    ('learning', 'Type of learning activity',
        {'display': 'learning', }),
)

METADATA_OPTION_CHOICES = [(x[0], x[1]) for x in ACTIVITY_METADATA]


class MetadataOption(models.Model):
    group = models.CharField(max_length=50, blank=False, choices=METADATA_OPTION_CHOICES)
    code = models.CharField(max_length=50, blank=False)
    title = models.CharField(max_length=255, blank=False)
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['group', 'position']
        unique_together = (('group', 'code'),)

    def __str__(self):
        return self.title


class MetadataOptionsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('position')


class ActivityQuerySet(TranslatableQuerySet):
    pass


class ActivityManager(PublishingManager, TranslatableManager):
    queryset_class = ActivityQuerySet


class Activity(TranslatableModel, PublishingModel, SpaceaweModel):  #,MediaAttachedModel

    uuid = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    code = models.CharField(unique=True, max_length=4, help_text='The 4 digit code that identifies the Activity, in the format "YY##": year, folowed by sequential number.')
    doi = models.CharField(blank=True, max_length=50, verbose_name='DOI', help_text='Digital Object Identifier, in the format XXXX/YYYY. See http://www.doi.org/')

    age = models.ManyToManyField(MetadataOption, limit_choices_to={'group': 'age'}, related_name='age+', )
    level = models.ManyToManyField(MetadataOption, limit_choices_to={'group': 'level'}, related_name='level+', help_text='Specify at least one of "Age" and "Level". ', )
    time = models.ForeignKey(MetadataOption, limit_choices_to={'group': 'time'}, related_name='+', blank=False, null=False, )
    group = models.ForeignKey(MetadataOption, limit_choices_to={'group': 'group'}, related_name='+', blank=True, null=True, )
    supervised = models.ForeignKey(MetadataOption, limit_choices_to={'group': 'supervised'}, related_name='+', blank=True, null=True, )
    cost = models.ForeignKey(MetadataOption, limit_choices_to={'group': 'cost'}, related_name='+', blank=True, null=True, )
    location = models.ForeignKey(MetadataOption, limit_choices_to={'group': 'location'}, related_name='+', blank=True, null=True, )
    skills = models.ManyToManyField(MetadataOption, limit_choices_to={'group': 'skills'}, related_name='skills+', verbose_name='core skills', )
    learning = models.ForeignKey(MetadataOption, limit_choices_to={'group': 'learning'}, related_name='+', blank=False, null=False, verbose_name='type of learning activity', help_text='Enquiry-based learning model', )

    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, null=True)

    sourcelink_name = models.CharField(max_length=255, blank=True, verbose_name='Source Name')
    sourcelink_url = models.URLField(max_length=255, blank=True, verbose_name='Source URL')

    objects = ActivityManager()

    def age_range(self):
        # return ' '.join(obj.title for obj in self.age.all())
        age_ranges = [obj.title for obj in self.age.all()]
        return utils.beautify_age_range(age_ranges)

    def author_list(self):
        result = []
        for item in self.authors.all():
            result.append(item.display_name())
        return '; '.join(result)

    def citable_author_list(self):
        result = []
        for item in self.authors.all():
            result.append(item.author.citable_name)
        return '; '.join(result)

    @property
    def main_visual(self):
        result = None
        images = self.attachment_set.filter(main_visual=True)
        if images:
            result = images[0].file
        return result

    def is_translation_fallback(self):
        return not self.has_translation(self.language_code)

    @property
    def sourcelink_caption(self):
        return self.sourcelink_name if self.sourcelink_name else self.sourcelink_url

    @classmethod
    def add_prefetch_related(self, qs, prefix=""):
        # # add _after_ qs.filter! see django docs on prefetch_related
        # if prefix:
        #     prefix += '__'
        # qs = qs.prefetch_related('%stranslations' % prefix)
        # qs = qs.prefetch_related('%scategories' % prefix)
        # qs = qs.prefetch_related('%scategories__translations' % prefix)
        # qs = qs.prefetch_related('%simages' % prefix)
        return qs

    def attachment_list(self):
        return self.attachment_set.filter(show=True)

    def metadata_aslist(self):
        result = []
        for meta_code, meta_title, meta_options in ACTIVITY_METADATA:
            value = None
            if meta_options.get('multiple', False):
                values = [x.title for x in getattr(self, meta_code).all()]
                value = ', '.join(values)
            else:
                display_name = meta_options.get('display', meta_code)
                display = getattr(self, display_name)
                if callable(display):
                    value = display()
                elif isinstance(display, MetadataOption):
                    value = display.title
                elif display:
                    value = display

            if value:
                result.append((meta_code, meta_title, value))
        return result

    def download_key(self):
        return self.slug + '-astroEDU-' + self.code

    def zip_url(self):
        return self.download_url('zip')
    def pdf_url(self):
        return self.download_url('pdf')
    def epub_url(self):
        return self.download_url('epub')
    def rtf_url(self):
        return self.download_url('rtf')

    def download_url(self, resource):
        return os.path.join(settings.MEDIA_URL, self.media_key(), 'download', self.download_key() + '.' + resource)
    def download_path(self, resource):
        return os.path.join(settings.MEDIA_ROOT, self.media_key(), 'download', self.download_key() + '.' + resource)

    def attachment_url(self, filename):
        if filename.startswith('http') or filename.startswith('/'):
            result = filename
        else:
            result = os.path.join(settings.MEDIA_URL, 'activities/attach', self.uuid, filename)
        return result

    def __str__(self):
        return '%s - %s' % (self.code, self.title)

    def get_absolute_url(self):
        return reverse('activities:detail', kwargs={'code': self.code, 'slug': self.slug, })

    # def get_absolute_url_full(self):
    #     return utils.get_qualified_url(self.get_absolute_url())

    def get_short_url_full(self):
        return utils.get_qualified_url('/a/%s' % self.code)

    def get_footer_disclaimer(self):
        return 'Go to %s for additional resources and download options of this activity.' % self.get_short_url_full()

    class Meta(PublishingModel.Meta):
        ordering = ['-code']
        verbose_name_plural = 'activities'


class ActivityTranslation(TranslatedFieldsModel):

    master = models.ForeignKey(Activity, related_name='translations', null=True)
    # slug = models.SlugField(unique=True, max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')
    slug = AutoSlugField(max_length=200, populate_from='title', always_update=True, unique=False)
    title = models.CharField(max_length=255, db_index=True, help_text='Title is shown in browser window. Use a good informative title, since search engines normally display the title on their result pages.')
    teaser = models.TextField(blank=False, max_length=140, help_text='One line, 140 characters maximum')
    theme = models.CharField(blank=False, max_length=40, help_text='Use top level AVM metadata')
    keywords = models.TextField(blank=False, help_text='List of keywords, separated by commas')

    acknowledgement = models.CharField(blank=True, max_length=255)

    description = models.TextField(blank=False, verbose_name='brief description', help_text='Maximum 2 sentences! Maybe what and how?')
    goals = models.TextField(blank=False, )
    objectives = models.TextField(blank=False, verbose_name='Learning Objectives', )
    evaluation = models.TextField(blank=True, help_text='If the teacher/educator wants to evaluate the impact of the activity, how can she/he do it?')
    materials = models.TextField(blank=True, help_text='Please indicate costs and/or suppliers if possible')
    background = models.TextField(blank=False, verbose_name='Background Information', )
    fulldesc = models.TextField(blank=False, verbose_name='Full Activity Description')
    curriculum = models.TextField(blank=True, verbose_name='Connection to school curriculum', help_text='Please indicate which country')
    additional_information = models.TextField(blank=True, help_text='Notes, Tips, Resources, Follow-up, Questions, Safety Requirements, Variations')
    conclusion = models.TextField(blank=False, )

    alert_message = models.TextField(blank=True, help_text='Alert message, do display at the top of the activity page')

    # Space Awareness fields
    big_idea = models.CharField(max_length=200, blank=True, verbose_name='Big Idea of Science')
    spaceawe_authorship = models.TextField(blank=True, verbose_name='Space Awareness authorship')

    class Meta:
        unique_together = (
            ('language_code', 'master'),
        )


@receiver(pre_save, sender=Activity)
def activity_pre_save(sender, instance, **kwargs):
    if instance.pk:
        old = Activity.objects.get(pk=instance.pk)
        redirect_activity(old, instance)


@receiver(post_save, sender=LogEntry)
def activity_post_save_delayed(sender, **kwargs):
    # The normal post_save signal is fired before the dependant objects are saved;
    # so instead we are listening to LogEntry post_save
    # In this case, we need the attachments to be up-to-date
    logentry = kwargs['instance']
    ct = ContentType.objects.get_for_model(Activity)
    if ct.id == logentry.content_type.id:
        instance = logentry.get_edited_object()
        # tasks.make_thumbnail.delay(instance)
        # tasks.zip_attachments.delay(instance)
        # tasks.make_epub.delay(instance)
        # tasks.make_pdf.delay(instance)
        # tasks.make_rtf.delay(instance)


def redirect_activity(old, new):
    if old.slug != new.slug:
        pass
        # current_site = Site.objects.get_current()

        # # new redirect
        # r = Redirect()
        # r.site = current_site
        # r.old_path = old.get_absolute_url()
        # r.new_path = new.get_absolute_url()
        # r.save()

        # #update any old redirects
        # for r in Redirect.objects.filter(new_path=old.get_absolute_url()):
        #     r.new_path = new.get_absolute_url()


class AuthorInstitution(models.Model):
    activity = models.ForeignKey(Activity, related_name='authors', )
    author = models.ForeignKey(Person)
    institution = models.ForeignKey(Institution)

    def display_name(self):
        return self.author.name + ', ' + self.institution.name

    def __str__(self):
        return self.display_name()


class Attachment(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(blank=True, upload_to=get_file_path_step, )
    main_visual = models.BooleanField(default=False, help_text='The main visual is used as the cover image.')
    show = models.BooleanField(default=False, verbose_name='Show', help_text='Include in attachment list.')
    position = models.PositiveSmallIntegerField(default=0, verbose_name='Position', help_text='Used to define the order of attachments in the attachment list.')
    hostmodel = models.ForeignKey(Activity)

    def display_name(self):
        if self.title:
            return self.title
        else:
            return os.path.basename(self.file.name)

    def __str__(self):
        return self.display_name()

    class Meta:
        ordering = ['-show', 'position', 'id']


class Collection(TranslatableModel, PublishingModel):
    activities = models.ManyToManyField(Activity, related_name='+', )
    # image = models.ForeignKey(ManagedFile, null=True)
    image = ImageField(null=True, blank=True, upload_to='collections')

    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    modification_date = models.DateTimeField(auto_now=True, null=True)

    @property
    def code(self):
        return self.slug

    @property
    def main_visual(self):
        return self.image.file if self.image else None

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
#        tasks.make_thumbnail.delay(self)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('collections:detail', args=[self.slug])

    class Meta(TranslatableModel.Meta):
        pass


class CollectionTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Collection, related_name='translations', null=True)
    title = models.CharField(blank=False, max_length=255)
    slug = models.SlugField(unique=True, db_index=True, help_text='Slug identifies the Collection; it is used as part of the URL. Use only lowercase characters.')
    # slug = AutoSlugField(max_length=200, populate_from='title', always_update=True, unique=False)
    description = models.TextField(blank=True, verbose_name='brief description', )


class Repository(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'repositories'


class RepositoryEntry(models.Model):
    repo = models.ForeignKey(Repository, blank=False, null=True)
    url = models.URLField(blank=False, max_length=255, )
    activity = models.ForeignKey(Activity)

    # def clean(self, *args, **kwargs):
    #     self.repo = None
    #     for name, value in settings.REPOSITORIES.items():
    #         url_pattern = value[1]
    #         if re.match(url_pattern, self.url):
    #             self.repo = name
    #     if not self.repo:
    #         raise ValidationError('Unknown repository URL. Known repositories are: ' + ', '.join(settings.REPOSITORIES.keys()))
    #     # super().clean(*args, **kwargs)

    def __str__(self):
        return '%s - %s' % (self.repo.name, self.url)

    class Meta:
        ordering = ['repo']
        verbose_name_plural = 'repository entries'
