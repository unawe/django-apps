# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0034_auto_20151022_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originalnewssource',
            name='slug',
            field=models.SlugField(max_length=200, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.'),
        ),
    ]
