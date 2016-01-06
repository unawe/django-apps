# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articletranslation',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
