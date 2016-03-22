# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0009_auto_20160215_2018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repository',
            options={'ordering': ['name'], 'verbose_name_plural': 'repositories'},
        ),
        migrations.AlterModelOptions(
            name='repositoryentry',
            options={'ordering': ['repo'], 'verbose_name_plural': 'repository entries'},
        ),
    ]
