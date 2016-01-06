# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0027_auto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, populate_from='title', editable=False),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='title',
            field=models.CharField(verbose_name='title', max_length=50),
        ),
    ]
