import os 

from django.db import models
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now
from django.conf import settings


def publishing_login_required():
    return lambda user: user and user.is_authenticated()


def publishing_group_required(group):
    return lambda user: user and user.groups.filter(name=group).exists()


def publishing_permission_required(perm, obj=None):
    return lambda user: user and user.has_perm(perm, obj)


def publishing_user_passes_test(test_func):
    return lambda user: test_func(user)


class PublishingManager(models.Manager):

    # only return objects that .is_released
    _query_public = Q(published=True) & \
        Q(release_date__lte=now) & \
        (Q(embargo_date__isnull=True) | Q(embargo_date__lte=now))
    # only return objects that .is_embargoed
    _query_embargoed = Q(published=True) & \
        Q(release_date__gt=now) & \
        (Q(embargo_date__isnull=True) | Q(embargo_date__lte=now))
    # return objects that are either .is_released and .is_embargoed
    _query_embargo_view = Q(published=True) & \
        (Q(embargo_date__isnull=True) | Q(embargo_date__lte=now))

    # def get_queryset(self):
    #     return super().get_queryset().filter(self._query_public)

    def featured(self):
        return self.filter(featured=True).order_by('-release_date')

    # I wanted to make this the default Manager, but that's not compatible with django-parler:
    # the TranslatableManager has use_for_related_fields=True
    def available(self, user=None):
        permission_all = self.model.PublishingMeta.permission_all
        permission_embargoed = self.model.PublishingMeta.permission_embargoed
        if permission_all and permission_all(user):
            result = super().get_queryset()
        elif permission_embargoed and permission_embargoed(user):
            result = super().get_queryset().filter(self._query_embargo_view)
        else:
            result = super().get_queryset().filter(self._query_public)
        return result

    def embargoed(self):
        return super().get_queryset().filter(self._query_embargoed)


class PublishingModel(models.Model):
    '''
    IMPORTANT: inherit before other classes.
    This is necessary when another parent class re-defines the default manager (objects) but was not designed to be cooperative.
    see https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
    '''
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    release_date = models.DateTimeField(blank=False)
    embargo_date = models.DateTimeField(blank=True, null=True)

    objects = PublishingManager()

    def is_released(self):
        return self.published and self.release_date <= now() and (self.embargo_date is None or self.embargo_date <= now())
    is_released.short_description = 'released?'
    is_released.boolean = True

    def is_embargoed(self):
        return self.published and self.release_date > now() and (self.embargo_date is None or self.embargo_date <= now())
    is_embargoed.short_description = 'embargoed?'
    is_embargoed.boolean = True

    def not_released_reason(self):
        result = []
        if not self.published:
            result.append('not published')
        if self.release_date > now():
            result.append('staging (release date in the future)')
        if self.is_embargoed():
            result.append('under embargo')
        return result

    @classmethod
    def sitemap(cls, priority=None):
        from django.contrib.sitemaps import GenericSitemap
        object_list = {
            'queryset': cls.objects.available(),  #TODO make sure this only shows _released objects
            'date_field': 'modification_date',
        }
        return GenericSitemap(object_list, priority=priority)

    class Meta:
        abstract = True
        ordering = ['-release_date']

    class PublishingMeta:
        permission_all = publishing_login_required()  # how to determine if a user can access all items
        permission_embargoed = None  # how to determine if a user can access embargoed items


class BaseAttachmentModel(models.Model):

    title = models.CharField(max_length=255, blank=True)
    show = models.BooleanField(default=False, verbose_name=u'Show', help_text=_(u'Include in attachment list.'))
    position = models.PositiveSmallIntegerField(default=0, verbose_name='Position', help_text=_(u'Used to define the order of attachments in the attachment list.'))
    # hostmodel = None  # must be set by concrete class! e.g.: models.ForeignKey(Activity)

    def display_name(self):
        if self.title:
            return self.title
        elif self.file:
            return os.path.basename(self.file.name)
        else:
            return os.path.basename(self.file.name)

    def __str__(self):
        return self.display_name()

    class Meta:
        abstract = True
        ordering = ['position', 'id']


class MediaAttachedModel(models.Model):

    # #TODO: simplify media_key: make it a constant string property of the concrete class, and remove most of MediaAttachedModel ?
    # @classmethod
    # def media_key(cls):
    #     return str(cls._meta.verbose_name_plural)

    # def media_url(self, resource, ext):
    #     if self.main_visual:
    #         return os.path.join(settings.MEDIA_URL, self.media_key(), resource, self.code) + '.' + ext

    #TODO: self.SIZES
    #TODO: 'jpg' magic number
    # def __getattribute__(self, name):
    #     # handles calls to e.g. 'thumb_url'
    #     if name[-4:] == '_url' and name[:-4] in self.SIZES:
    #         return self.media_url(name[:-4], 'jpg')
    #     else:
    #         return super().__getattribute__(name)

    @property
    def main_visual(self):
        result = None
        images = self.images.all()
        if images:
            result = images[0].file
        return result

    def image_list(self):
        return self.images.filter(show=True)

    def attachment_list(self):
        return self.attachment_set.filter(show=True)

    class Meta:
        abstract = True
