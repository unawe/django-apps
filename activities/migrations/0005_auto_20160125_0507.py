# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
        ('activities', '0004_auto_20160124_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='big_idea',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='theme',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='collectiontranslation',
            name='slug',
            field=models.SlugField(help_text='Slug identifies the Collection; it is used as part of the URL. Use only lowercase characters.', unique=True),
        ),
    ]
