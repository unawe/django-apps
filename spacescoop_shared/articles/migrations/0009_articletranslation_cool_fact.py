# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20150709_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletranslation',
            name='cool_fact',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
