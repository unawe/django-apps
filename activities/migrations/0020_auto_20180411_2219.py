# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0019_remove_journeychaptertranslation_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journeycategory',
            options={'verbose_name': 'journey category', 'verbose_name_plural': 'journey category'},
        ),
    ]
