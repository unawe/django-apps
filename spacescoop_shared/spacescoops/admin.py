import re

from django.contrib import admin
from django import forms
from parler.admin import TranslatableAdmin
from parler.forms import TranslatableModelForm
from parler.widgets import SortedCheckboxSelectMultiple
# from parler.admin import SortedRelatedFieldListFilter
from sorl.thumbnail.admin import AdminImageMixin

# from django_ext.adminutils import download_csv

from .models import Article, Image, OriginalNewsSource, OriginalNews, Category, DEFAULT_TRANSLATION_CREDITS


@admin.register(OriginalNewsSource)
class OriginalNewsSourceAdmin(TranslatableAdmin, AdminImageMixin):
    def logo_embed(self, obj):
        if obj.logo:
            return '<img src="%s" style="height:50px" />' % obj.logo.image.icons['64']
    logo_embed.short_description = 'Logo'
    logo_embed.allow_tags = True

    list_display = ('name', 'fullname', 'url', 'all_languages_column', ) #'logo_embed', ) #'admin_logo', )
    list_editable = ('url', )
    ordering = ('name', )
    prepopulated_fields = {'slug': ('name', ), }


class OriginalNewsInlineAdmin(admin.TabularInline):
    model = OriginalNews
    fields = ('original_news_source', 'url', )
    extra = 1


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ('title', 'all_languages_column', 'position', )
    list_editable = ('position', )
    # list_display = ('title', ), 'all_languages_column', )

    fieldsets = (
        (None,
            {'fields': ('title', ), }),
    )

    # def get_prepopulated_fields(self, request, obj=None):
    #     # can't use `prepopulated_fields = ..` because it breaks the admin validation
    #     # for translated fields. This is the official django-parler workaround.
    #     return {
    #         'slug': ('title',)
    #     }

    def has_add_permission(self, request):
        return False

# class ArticleImageInlineFormset(forms.models.BaseInlineFormSet):
#     def clean(self):
#         # There can be only one "main visual"
#         if any(self.errors):
#             # Don't bother validating the formset unless each form is valid on its own
#             return
#
#         main_visual_count = 0
#         for form in self.forms:
#             if form.cleaned_data:
#                 main_visual = form.cleaned_data['main_visual']
#                 if main_visual:
#                     main_visual_count += 1
#
#         if main_visual_count > 1:
#             raise forms.ValidationError('There can be only one "main visual".')


class ArticleImageInline(admin.TabularInline):
    model = Image
    # formset = ArticleImageInlineFormset
    fields = ('title', 'file', 'position', )
    min_num = 2
    extra = 1


# class ArticleAttachmentInline(admin.TabularInline):
#     model = Attachment
#     fields = ('title', 'file', 'position', )


class ArticleAdminForm(TranslatableModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.language_code in DEFAULT_TRANSLATION_CREDITS:
            self.initial['translation_credit_text'] = DEFAULT_TRANSLATION_CREDITS[self.language_code]['text']
            self.initial['translation_credit_url'] = DEFAULT_TRANSLATION_CREDITS[self.language_code]['url']

    def clean_code(self):
        code = self.cleaned_data['code']
        if not re.match('^\w*\d{4}$', code):
            raise forms.ValidationError('The code should be four digits, in the format: YY##')
        return code

    class Meta:
        model = Article
        fields = ('code', 'title', 'release_date', 'published', 'featured', 'story', 'cool_fact', 'translation_credit_text', 'translation_credit_url', 'categories', 'spaceawe_category', 'tags', )
        widgets = {
            'categories': SortedCheckboxSelectMultiple,
            #TODO: django-parler seems to be replacing the default css class when Meta is defined...
            'title': forms.TextInput(attrs={'class': 'vTextField', }),
            # 'slug': forms.TextInput(attrs={'class': 'vTextField', }),
            'translation_credit_text': forms.TextInput(attrs={'class': 'vTextField', }),
            'translation_credit_url': forms.TextInput(attrs={'class': 'vTextField', }),
        }


def _admin_datetime_format(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S %Z') if dt else None


@admin.register(Article)
class ArticleAdmin(TranslatableAdmin):

    def get_queryset(self, request):
        qs = super().queryset(request)
        qs = Article.add_prefetch_related(qs)
        return qs

    def release_date_fmt(self, obj):
        return _admin_datetime_format(obj.release_date)
    release_date_fmt.admin_order_field = 'release_date'
    release_date_fmt.short_description = 'Release Date'

    # def main_visual_embed(self, obj):
    #     if obj.main_visual:
    #         return '<img src="%s" style="height:50px" />' % obj.main_visual.file.icons['64']
    # main_visual_embed.short_description = 'Image'
    # main_visual_embed.allow_tags = True

    # list_display = ('code', 'title', 'all_languages_column', 'language_column', 'is_released', 'release_date_fmt', 'published', 'featured', )
    list_display = ('code', 'title', 'all_languages_column', 'is_released', 'release_date_fmt', 'published', 'featured', )
    # list_display = ('code', 'title', 'is_released', 'release_date_fmt', 'published', 'featured', 'main_visual_embed', )
    date_hierarchy = 'release_date'
    # list_filter = (
    #     'categories',
    #     # ('categories', SortedRelatedFieldListFilter),
    # )
    search_fields = ('code', 'translations__title', )

    # actions = (download_csv, )

    form = ArticleAdminForm

    inlines = (
        OriginalNewsInlineAdmin,
        ArticleImageInline,
        # ArticleAttachmentInline,
    )

    fieldsets = (
        (None,
            {'fields': ('code', 'title', ), }),
        ('Publishing',
            {'fields': (('release_date', ),
                        ('published', 'featured', ),), }),
        (None,
            {'fields': ('story', 'cool_fact', ), }),
        ('Translation credits',
            {'fields': ('translation_credit_text', 'translation_credit_url', )}),
        (None,
            {'fields': ('categories', 'spaceawe_category', 'tags', ), }),
    )
    readonly_fields = ('creation_date', 'modification_date', 'is_released', )

    # def get_prepopulated_fields(self, request, obj=None):
    #     # can't use `prepopulated_fields = ..` because it breaks the admin validation
    #     # for translated fields. This is the official django-parler workaround.
    #     return {
    #         'slug': ('title',)
    #     }
