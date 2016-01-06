# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0021_auto_20150927_2303'),
    ]

    operations = [
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
            field=models.DateTimeField(null=True, auto_now_add=True),
        ),
        migrations.AddField(
            model_name='articletranslation',
            name='modification_date',
            field=models.DateTimeField(null=True, auto_now=True),
        ),
    ]
