# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20150708_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletranslation',
            name='slug',
            field=models.SlugField(max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', default=None, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem', verbose_name='Tags', blank=True),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
