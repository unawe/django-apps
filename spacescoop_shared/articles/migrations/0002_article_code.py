# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='code',
            field=models.CharField(default=None, help_text='The 4 digit code that identifies the Activity, in the format "YY##": year, folowed by sequential number.', max_length=4),
            preserve_default=False,
        ),
    ]
