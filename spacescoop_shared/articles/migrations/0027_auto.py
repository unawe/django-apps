# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0026_auto_20150928_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(max_length=255, editable=False, populate_from='title', always_update=True),
        ),
    ]
