# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('articles', '0013_auto_20150915_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='originalnewssource',
            name='logo',
            field=filer.fields.image.FilerImageField(related_name='news_source_logo', null=True, to='filer.Image', blank=True),
        ),
    ]
