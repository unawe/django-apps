# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import taggit_autosuggest.managers
import spacescoop_shared.articles.models
import datetime
import autoslug.fields
import sorl.thumbnail.fields
import uuid
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('articles', '0001_initial'), ('articles', '0002_article_code'), ('articles', '0003_auto_20150624_1937'), ('articles', '0004_auto_20150629_2000'), ('articles', '0005_auto_20150629_2241'), ('articles', '0006_auto_20150629_2247'), ('articles', '0007_auto_20150708_1505'), ('articles', '0008_auto_20150709_1145'), ('articles', '0009_articletranslation_cool_fact'), ('articles', '0010_auto_20150711_1058'), ('articles', '0011_auto_20150714_1706'), ('articles', '0012_auto_20150914_1823'), ('articles', '0013_auto_20150915_1844'), ('articles', '0014_originalnewssource_logo'), ('articles', '0015_image'), ('articles', '0016_auto_20150916_1555'), ('articles', '0017_auto_20150921_1522'), ('articles', '0018_auto_20150924_1030'), ('articles', '0019_article_categories'), ('articles', '0020_remove_article_uuid'), ('articles', '0021_auto_20150927_2303'), ('articles', '0022_auto_20150928_1227'), ('articles', '0023_auto_20150928_1511'), ('articles', '0024_auto_20150928_1546'), ('articles', '0025_auto_20150928_1648'), ('articles', '0026_auto_20150928_1650'), ('articles', '0027_auto'), ('articles', '0028_auto_20150928_1727'), ('articles', '0029_auto_20150928_1734'), ('articles', '0030_auto_20151006_1430'), ('articles', '0031_auto_20151014_1831'), ('articles', '0032_auto_20151021_1709'), ('articles', '0033_originalnewssource_article_count'), ('articles', '0034_auto_20151022_1442'), ('articles', '0035_auto_20151022_1443'), ('articles', '0036_auto_20151119_1108'), ('articles', '0037_auto_20151203_1518'), ('articles', '0038_auto_20160106_2206'), ('articles', '0039_auto_20160109_1200'), ('articles', '0040_auto_20160109_1200')]

    dependencies = [
        ('taggit', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('title', models.CharField(max_length=255)),
                ('master', models.ForeignKey(editable=False, null=True, related_name='translations', to='articles.Article')),
            ],
            options={
                'verbose_name': 'article Translation',
                'db_table': 'articles_articletranslation',
                'managed': True,
                'default_permissions': (),
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='article',
            name='code',
            field=models.CharField(help_text='The 4 digit code that identifies the Article, in the format "YY##": year, folowed by sequential number.', max_length=4),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='title',
            field=models.CharField(verbose_name='Title', max_length=255),
        ),
        migrations.AddField(
            model_name='article',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='embargo_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 19, 0, 4, 713618, tzinfo=utc)),
            preserve_default=False,
        ),

        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(verbose_name='Tags', help_text='A comma-separated list of tags.', blank=True, through='taggit.TaggedItem', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='story',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='slug',
            field=models.SlugField(unique=True, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='title',
            field=models.CharField(verbose_name='title', max_length=255),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='cool_fact',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.CreateModel(
            name='OriginalNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('url', models.CharField(verbose_name='URL', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'original news',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewsSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='translation_credit_text',
            field=models.CharField(help_text='If set, this text will replace the default translation for credits.', blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='translation_credit_url',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AddField(
            model_name='originalnews',
            name='original_news_source',
            field=models.ForeignKey(to='articles.OriginalNewsSource'),
        ),
        migrations.AddField(
            model_name='originalnews',
            name='article',
            field=models.ForeignKey(to='articles.Article'),
        ),
        migrations.AddField(
            model_name='article',
            name='original_news',
            field=models.ManyToManyField(through='articles.OriginalNews', to='articles.OriginalNewsSource'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('main_visual', models.BooleanField(help_text='The main visual is used as the cover image.', default=False)),
                ('show', models.BooleanField(verbose_name='Show', help_text='Include in attachment list.', default=False)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Position', help_text='Used to define the order of attachments in the attachment list.', default=0)),
                ('hostmodel', models.ForeignKey(to='articles.Article')),
            ],
            options={
                'ordering': ['-show', 'position', 'id'],
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position', 'id']},
        ),
        migrations.RemoveField(
            model_name='image',
            name='main_visual',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('slug', models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=255)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='articles.Category')),
            ],
        ),
        migrations.AlterModelOptions(
            name='articletranslation',
            options={},
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='master',
            field=models.ForeignKey(null=True, related_name='translations', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'master')]),
        ),
        migrations.AlterModelTable(
            name='articletranslation',
            table=None,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='articles.Category'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, unique_with=('language_code',), editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, unique_with=('language_code',), editable=False, populate_from='title'),
        ),
        migrations.RemoveField(
            model_name='article',
            name='creation_date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='modification_date',
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='translation_credit_text',
            field=models.CharField(help_text='If set, this text will replace the default translation for credits.', blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='translation_credit_url',
            field=models.CharField(max_length=255, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='cool_fact',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title'),
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='title',
            field=models.CharField(verbose_name='title', max_length=50),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title'),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='title',
            field=models.CharField(verbose_name='title', max_length=200),
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-release_date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='articles.Category'),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='title',
            field=models.CharField(verbose_name='title', max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='hostmodel',
            field=models.ForeignKey(related_name='images', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(help_text='The 4 digit code that identifies the Article, in the format "YY##": year, folowed by sequential number.', db_index=True, max_length=4),
        ),
        migrations.CreateModel(
            name='OriginalNewsSourceTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language_code', models.CharField(verbose_name='Language', max_length=15, db_index=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='articles.OriginalNewsSource')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='originalnewssourcetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AddField(
            model_name='originalnewssource',
            name='article_count',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='originalnewssource',
            name='slug',
            field=models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=200),
        ),
        migrations.AlterField(
            model_name='originalnewssource',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterModelOptions(
            name='originalnewssource',
            options={'verbose_name': 'partner'},
        ),
        migrations.AddField(
            model_name='originalnewssource',
            name='fullname',
            field=models.CharField(help_text='If set, the full name will be used in some places instead of the name', blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='original_news',
            field=models.ManyToManyField(related_name='articles', through='articles.OriginalNews', to='articles.OriginalNewsSource'),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories', 'ordering': ('position',)},
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='originalnewssource',
            name='name',
            field=models.CharField(help_text='Short (and commonly used) name', unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='originalnewssourcetranslation',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='Text to appear in Parnet page', blank=True, null=True),
        ),
        migrations.AlterModelOptions(
            name='originalnewssourcetranslation',
            options={'verbose_name': 'partner translation'},
        ),
        migrations.AddField(
            model_name='article',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='image',
            name='file',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to=spacescoop_shared.articles.models.get_file_path_article_attachment, null=True),
        ),
        migrations.AddField(
            model_name='originalnewssource',
            name='logo',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='partners', null=True),
        ),
    ]
