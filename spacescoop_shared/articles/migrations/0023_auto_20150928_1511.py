# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0022_auto_20150928_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='originalnews',
            old_name='release',
            new_name='article',
        ),
    ]
