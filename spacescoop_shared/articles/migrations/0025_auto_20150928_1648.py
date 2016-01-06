# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0024_auto_20150928_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='cool_fact',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
