# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_auto_20150924_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='articles.Category'),
        ),
    ]
