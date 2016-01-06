# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_ext.models
import taggit_autosuggest.managers
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20150711_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(blank=True)),
                ('main_visual', models.BooleanField(help_text='The main visual is used as the cover image.', default=False)),
                ('show', models.BooleanField(help_text='Include in attachment list.', verbose_name='Show', default=False)),
                ('position', models.PositiveSmallIntegerField(help_text='Used to define the order of attachments in the attachment list.', verbose_name='Position', default=0)),
            ],
            options={
                'abstract': False,
                'ordering': ['-show', 'position', 'id'],
            },
        ),
        migrations.RemoveField(
            model_name='lowercasetaggeditem',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='lowercasetaggeditem',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='uuid',
            field=models.UUIDField(editable=False, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=taggit_autosuggest.managers.TaggableManager(help_text='A comma-separated list of tags.', to='taggit.Tag', through='taggit.TaggedItem', blank=True, verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='LowerCaseTag',
        ),
        migrations.DeleteModel(
            name='LowerCaseTaggedItem',
        ),
        migrations.AddField(
            model_name='attachment',
            name='hostmodel',
            field=models.ForeignKey(to='articles.Article'),
        ),
    ]
