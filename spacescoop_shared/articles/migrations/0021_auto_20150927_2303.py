# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0020_remove_article_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, populate_from='title', editable=False, unique_with=('language_code',)),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, populate_from='title', editable=False, unique_with=('language_code',)),
        ),
    ]
