# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150624_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='embargo_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='modification_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 29, 19, 0, 4, 713618, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
