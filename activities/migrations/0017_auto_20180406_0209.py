# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_auto_20180328_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeychapter',
            name='embargo_date',
        ),
        migrations.RemoveField(
            model_name='journeychapter',
            name='featured',
        ),
        migrations.RemoveField(
            model_name='journeychapter',
            name='published',
        ),
        migrations.RemoveField(
            model_name='journeychapter',
            name='release_date',
        ),
        migrations.AddField(
            model_name='journeycategory',
            name='embargo_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='journeycategory',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeycategory',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='journeycategory',
            name='release_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 6, 0, 9, 33, 653066, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
