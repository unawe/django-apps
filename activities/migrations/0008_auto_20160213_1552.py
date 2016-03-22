# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0007_auto_20160126_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='sourcelink_name',
            field=models.CharField(max_length=255, verbose_name='Source Name', blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='sourcelink_url',
            field=models.URLField(max_length=255, verbose_name='Source URL', blank=True),
        ),
    ]
