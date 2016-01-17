# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import autoslug.fields
import spacescoop_shared.articles.models
import taggit_autosuggest.managers
import uuid
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('uuid', models.UUIDField(editable=False, default=uuid.uuid4)),
                ('code', models.CharField(db_index=True, max_length=4, help_text='The 4 digit code that identifies the Article, in the format "YY##": year, folowed by sequential number.')),
            ],
            options={
                'ordering': ['-release_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, always_update=True, populate_from='title', max_length=200)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('story', ckeditor.fields.RichTextField()),
                ('cool_fact', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('translation_credit_text', models.CharField(blank=True, max_length=255, help_text='If set, this text will replace the default translation for credits.', null=True)),
                ('translation_credit_url', models.CharField(blank=True, max_length=255, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modification_date', models.DateTimeField(auto_now=True, null=True)),
                ('master', models.ForeignKey(related_name='translations', to='articles.Article', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('position', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('position',),
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('slug', autoslug.fields.AutoSlugField(max_length=200, always_update=True, populate_from='title', unique_with=('language_code',), editable=False)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('master', models.ForeignKey(related_name='translations', to='articles.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('show', models.BooleanField(verbose_name='Show', help_text='Include in attachment list.', default=False)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Position', help_text='Used to define the order of attachments in the attachment list.', default=0)),
                ('file', sorl.thumbnail.fields.ImageField(blank=True, upload_to=spacescoop_shared.articles.models.get_file_path_article_attachment, null=True)),
                ('hostmodel', models.ForeignKey(related_name='images', to='articles.Article')),
            ],
            options={
                'ordering': ['position', 'id'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OriginalNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('url', models.CharField(max_length=255, verbose_name='URL')),
                ('article', models.ForeignKey(to='articles.Article')),
            ],
            options={
                'verbose_name_plural': 'original news',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewsSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(unique=True, help_text='Short (and commonly used) name', max_length=200)),
                ('slug', models.SlugField(max_length=200, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')),
                ('fullname', models.CharField(blank=True, max_length=200, help_text='If set, the full name will be used in some places instead of the name')),
                ('url', models.CharField(max_length=255)),
                ('logo', sorl.thumbnail.fields.ImageField(blank=True, upload_to='partners', null=True)),
                ('article_count', models.IntegerField(editable=False, default=0)),
            ],
            options={
                'verbose_name': 'partner',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewsSourceTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, help_text='Text to appear in Parnet page')),
                ('master', models.ForeignKey(related_name='translations', to='articles.OriginalNewsSource', null=True)),
            ],
            options={
                'verbose_name': 'partner translation',
            },
        ),
        migrations.AddField(
            model_name='originalnews',
            name='original_news_source',
            field=models.ForeignKey(to='articles.OriginalNewsSource'),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='articles.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='original_news',
            field=models.ManyToManyField(through='articles.OriginalNews', related_name='articles', to='articles.OriginalNewsSource'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(through='taggit.TaggedItem', help_text='A comma-separated list of tags.', to='taggit.Tag', blank=True, verbose_name='Tags'),
        ),
        migrations.AlterUniqueTogether(
            name='originalnewssourcetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'slug')]),
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
