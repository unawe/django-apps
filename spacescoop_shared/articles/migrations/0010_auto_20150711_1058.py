# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit_autosuggest.managers


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('articles', '0009_articletranslation_cool_fact'),
    ]

    operations = [
        migrations.CreateModel(
            name='LowerCaseTag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LowerCaseTaggedItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', verbose_name='Content type', related_name='articles_lowercasetaggeditem_tagged_items')),
                ('tag', models.ForeignKey(related_name='tagged_items', to='articles.LowerCaseTag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(to='articles.LowerCaseTag', through='articles.LowerCaseTaggedItem', help_text='A comma-separated list of tags.', blank=True, verbose_name='Tags'),
        ),
    ]
