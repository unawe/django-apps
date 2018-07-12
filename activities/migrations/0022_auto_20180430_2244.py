# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0021_auto_20180430_2221'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journeychapter',
            options={},
        ),
        migrations.AlterField(
            model_name='journeycategorytranslation',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='General introduction', null=True),
        ),
    ]
