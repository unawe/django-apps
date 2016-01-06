# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0028_auto_20150928_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', always_update=True),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
    ]
