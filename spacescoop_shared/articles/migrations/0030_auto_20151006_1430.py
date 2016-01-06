# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0029_auto_20150928_1734'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-release_date']},
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(related_name='articles', to='articles.Category'),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='image',
            name='hostmodel',
            field=models.ForeignKey(related_name='images', to='articles.Article'),
        ),
    ]
