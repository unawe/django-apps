import re

from django_mistune import markdown

from django.contrib import admin
from django import forms
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm
from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings

from contrib.remainingcharacters.admin import CounterAdmin
# from contrib.adminutils import download_csv

from .models import Activity, Attachment, LanguageAttachment, AuthorInstitution, MetadataOption, Collection, RepositoryEntry, Repository
# from activities.models import Richtext
# from filemanager.models import File as ManagedFile
from activities.utils import bleach_clean

from parler.admin import TranslatableTabularInline

# class RichtextAdminForm(forms.ModelForm):
#     from pagedown.widgets import AdminPagedownWidget
#     field4 = forms.CharField(widget=AdminPagedownWidget())        

#     class Meta:
#         model = Richtext


# class RichtextAdmin(admin.ModelAdmin):
#     # from django.db import models

#     # import django_markdown.widgets
#     # formfield_overrides = {
#     #     models.TextField: {'widget': django_markdown.widgets.MarkdownWidget()},
#     # }

#     # from pagedown.widgets import AdminPagedownWidget
#     # formfield_overrides = {
#     #     models.TextField: {'widget': AdminPagedownWidget },
#     # }
#     form = RichtextAdminForm


class MetadataOptionAdmin(admin.ModelAdmin):
    model = MetadataOption
    list_display = ('code', 'title', 'group', 'position', )
    list_editable = ('position', )
    list_filter = ('group',)

    def has_add_permission(self, request):
        return False


class ActivityAttachmentInlineFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        if any(self.errors):
            # Don't bother validating the formset unless each form is valid on its own
            return

        # There can be only one "main visual"
        main_visual_count = 0
        for form in self.forms:
            if form.cleaned_data:
                main_visual = form.cleaned_data['main_visual']
                if main_visual:
                    main_visual_count += 1

        if main_visual_count > 1:
            raise forms.ValidationError('There can be only one "main visual".')


class AuthorInstitutionInline(admin.TabularInline):
    model = AuthorInstitution
    verbose_name = 'author'
    verbose_name_plural = 'authors'
    min_num = 1
    extra = 1


class ActivityAttachmentInline(admin.TabularInline):
    model = Attachment
    formset = ActivityAttachmentInlineFormset
    fields = ('title', 'file', 'main_visual', 'show', 'position', )


class ActivityLanguageAttachmentInline(TranslatableTabularInline):
    model = LanguageAttachment
    fields = ('title', 'file', 'main_visual', 'show', 'position', )


class RepositoryEntryInline(admin.TabularInline):
    model = RepositoryEntry


class ActivityAdminForm(TranslatableModelForm):

    class Meta:
        model = Activity
        fields = ('code', 'title', 'release_date', 'published', 'featured', 'description', 'materials', 'goals', 'objectives', 'background', 'fulldesc', 'evaluation', 'curriculum', 'additional_information', 'conclusion', 'space', 'earth', 'navigation', 'heritage', 'sourcelink_name', 'sourcelink_url', )
        widgets = {
            'time': forms.RadioSelect,
            'group': forms.RadioSelect,
            'supervised': forms.RadioSelect,
            'cost': forms.RadioSelect,
            'location': forms.RadioSelect,
            'learning': forms.RadioSelect,
            'teaser': forms.TextInput(attrs={'class': 'vTextField'}),
        }

    def clean_code(self):
        code = self.cleaned_data['code']
        if not re.match('^\w*\d{4}$', code):
            raise forms.ValidationError('The code should be four digits, in the format: YY##')
        return code

    def clean_teaser(self):
        teaser = self.cleaned_data['teaser']
        teaser = teaser.replace('\n', ' ').strip()
        return teaser

    def clean(self):
        cleaned_data = super().clean()

        age = cleaned_data.get('age')
        level = cleaned_data.get('level')
        if not age and not level:
            raise forms.ValidationError('Please fill in at least one of these fields: "Age", "Level"')

        for fieldname in ('description', 'materials', 'goals', 'objectives', 'background', 'fulldesc', 'evaluation', 'curriculum', 'additional_information', 'conclusion', ):
            value = cleaned_data.get(fieldname)
            value = bleach_clean(value)  # sanitize html embed in markdown
            cleaned_data[fieldname] = value
            try:
                markdown(value)
            except:
                # TODO: test error logging!
                import sys
                e = sys.exc_info()[0]
                print(e)
                self.add_error(fieldname, _('Markdown error'))

        return cleaned_data


class MembershipInline(admin.TabularInline):
    model = Collection.activities.through


class ActivityAdmin(TranslatableAdmin):

    def view_on_site(self, obj):
        return obj.get_absolute_url()

    def view_link(self, obj):
        return '<a href="%s">View</a>' % obj.get_absolute_url()
    view_link.short_description = ''
    view_link.allow_tags = True

    # def thumb_embed(self, obj):
    #     if obj.main_visual:
    #         return '<img src="%s" style="height:50px" />' % obj.thumb_url()
    # thumb_embed.short_description = 'Thumbnail'
    # thumb_embed.allow_tags = True

    counted_fields = ('teaser', )

    form = ActivityAdminForm
    list_display = ('code', 'title', 'all_languages_column', 'author_list', 'published', 'release_date', 'is_released', 'featured', 'doi', 'view_link', )  # , 'thumb_embed', 'list_link_thumbnail', view_link('activities'))
    list_editable = ('published', 'featured', )
    ordering = ('-release_date', )
    date_hierarchy = 'release_date'
    list_filter = ('age', 'level', 'time', 'group', 'supervised', 'cost', 'location', )
    # actions = (download_csv, )  #NOT WORKING with django-parler

    if settings.SHORT_NAME == 'astroedu':
        inlines = [AuthorInstitutionInline, ActivityAttachmentInline, RepositoryEntryInline, MembershipInline, ]
    else:
        inlines = [AuthorInstitutionInline, ActivityAttachmentInline, ActivityLanguageAttachmentInline, RepositoryEntryInline, ]

    # activities is shared model, but on astroedu is needed modified fieldset
    if settings.SHORT_NAME == 'astroedu':
        fieldsets = [
            (None,
             {'fields': ('code', 'title',)}),
            ('Publishing',
             {'fields': ('published', 'featured', ('release_date', 'embargo_date'),),}),
            (None,
             {'fields': (
                 ('age', 'level',), ('time', 'group', 'supervised', 'cost',), ('location', 'skills', 'learning',),
                 'keywords')}),
            ('Description',
             {'fields': (
                 'theme', 'teaser', 'description', 'goals', 'objectives', 'evaluation', 'materials', 'background',)}),
            (None,
             {'fields': ('fulldesc',)}),
            (None,
             {'fields': ('curriculum', 'additional_information', 'conclusion',)}),
        ]
    else:
        fieldsets = [
            (None,
             {'fields': ('code', 'title',)}),
            ('Publishing',
             {'fields': ('published', 'featured', ('release_date', 'embargo_date'),),}),
            (None,
             {'fields': (
                 ('age', 'level',), ('time', 'group', 'supervised', 'cost',), ('location', 'skills', 'learning',),
                 'keywords', 'big_idea',)}),
            ('Description',
             {'fields': (
                 'theme', 'teaser', 'description', 'goals', 'objectives', 'evaluation', 'materials', 'background',)}),
            (None,
             {'fields': ('fulldesc',)}),
            (None,
             {'fields': ('curriculum', 'additional_information', 'conclusion',)}),
            ('Source',
             {'fields': ('spaceawe_authorship', ('sourcelink_name', 'sourcelink_url',),)}),
        ]



    readonly_fields = ('is_released', )
    # richtext_fields = ('description', 'materials', 'objectives', 'background', 'fulldesc_intro', 'fulldesc_outro', 'additional_information', 'evaluation', 'curriculum', 'credit', )
    formfield_overrides = {
        models.ManyToManyField: {'widget': forms.CheckboxSelectMultiple},
    }

    fieldsets_and_inlines_order = ('f', 'f', 'i', )  # order of fields: first fieldset, then first inline, then everything else as usual

    class Media:
        js = [
            # '/static/js/jquery-1.7.2.min',
            'http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js',
            '/static/js/admin.js',
            # '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            # '/static/grappelli/tinymce_setup/tinymce_setup.js',
        ]


class CollectionAdminForm(TranslatableModelForm):

    def clean(self):
        cleaned_data = super().clean()
        slug = cleaned_data.get('slug')
        if not re.match('^[a-z]+$', slug):
            raise forms.ValidationError('The slug must contain only lowercase characters')
        return cleaned_data


class CollectionAdmin(TranslatableAdmin):
    form = CollectionAdminForm

    def view_link(self, obj):
        return '<a href="%s">View</a>' % obj.get_absolute_url()

    view_link.short_description = ''
    view_link.allow_tags = True

    list_display = ('title', 'slug', 'view_link', )  # 'thumb_embed',

    fieldsets = [
        (None, {'fields': ('title', 'slug', )}),
        ('Publishing', {'fields': ('published', 'featured', ('release_date', 'embargo_date'), ), }),
        ('Contents', {'fields': ('description', 'image', )}),
    ]

    #inlines = [
    #    MembershipInline,
    #]

    #exclude = ('activities',)


if settings.SHORT_NAME == 'astroedu':
    admin.site.register(Collection, CollectionAdmin)
    ActivityAdmin.fieldsets = ActivityAdmin.fieldsets[0:1] + [
        (None,
            {'fields': ('acknowledgement', 'doi', )}),
        ] + ActivityAdmin.fieldsets[1:]
elif settings.SHORT_NAME == 'spaceawe':
    ActivityAdmin.fieldsets = ActivityAdmin.fieldsets[0:1] + [
        (None,
            {'fields': ('alert_message', )}),
        ('Space Awareness Category',
            {'fields': (('space', 'earth', 'navigation', 'heritage', ), )})
        ] + ActivityAdmin.fieldsets[1:]


admin.site.register(MetadataOption, MetadataOptionAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Repository)
