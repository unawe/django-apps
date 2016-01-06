# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20150916_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='story',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
