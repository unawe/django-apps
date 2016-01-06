# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import spacescoop_shared.articles.models
import django_ext.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_auto_20150714_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalNews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(verbose_name='URL', max_length=255)),
            ],
            options={
                'verbose_name_plural': 'original news',
            },
        ),
        migrations.CreateModel(
            name='OriginalNewsSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='translation_credit_text',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='translation_credit_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(max_length=4, help_text='The 4 digit code that identifies the Article, in the format "YY##": year, folowed by sequential number.'),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(blank=True, upload_to=spacescoop_shared.articles.models.get_file_path_article_attachment),
        ),
        migrations.AddField(
            model_name='originalnews',
            name='original_news_source',
            field=models.ForeignKey(to='articles.OriginalNewsSource'),
        ),
        migrations.AddField(
            model_name='originalnews',
            name='release',
            field=models.ForeignKey(to='articles.Article'),
        ),
        migrations.AddField(
            model_name='article',
            name='original_news',
            field=models.ManyToManyField(through='articles.OriginalNews', to='articles.OriginalNewsSource'),
        ),
    ]
