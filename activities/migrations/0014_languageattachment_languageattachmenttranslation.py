# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import activities.models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0013_alert_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='LanguageAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('main_visual', models.BooleanField(default=False, help_text='The main visual is used as the cover image.')),
                ('show', models.BooleanField(default=False, verbose_name='Show', help_text='Include in attachment list.')),
                ('position', models.PositiveSmallIntegerField(default=0, verbose_name='Position', help_text='Used to define the order of attachments in the attachment list.')),
                ('hostmodel', models.ForeignKey(to='activities.Activity')),
            ],
            options={
                'ordering': ['-show', 'position', 'id'],
            },
        ),
        migrations.CreateModel(
            name='LanguageAttachmentTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('file', models.FileField(upload_to=activities.models.get_translated_file_path_step, blank=True)),
                ('master', models.ForeignKey(related_name='translations', to='activities.LanguageAttachment', null=True)),
            ],
            options={
                'default_permissions': (),
                'abstract': False,
            },
        ),
    ]
