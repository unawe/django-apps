# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0018_journeycategorytranslation_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeychaptertranslation',
            name='slug',
        ),
    ]
