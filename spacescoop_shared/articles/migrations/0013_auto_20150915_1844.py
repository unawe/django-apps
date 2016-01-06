# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20150914_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='originalnewssource',
            name='logo',
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='translation_credit_text',
            field=models.CharField(blank=True, help_text='If set, this text will replace the default translation for credits.', max_length=255),
        ),
    ]
