# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0023_auto_20150928_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='translation_credit_text',
            field=models.CharField(max_length=255, help_text='If set, this text will replace the default translation for credits.', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='translation_credit_url',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
