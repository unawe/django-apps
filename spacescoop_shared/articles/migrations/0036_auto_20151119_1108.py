# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0035_auto_20151022_1443'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='originalnewssource',
            options={'verbose_name': 'partner'},
        ),
        migrations.AddField(
            model_name='originalnewssource',
            name='fullname',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='original_news',
            field=models.ManyToManyField(to='articles.OriginalNewsSource', related_name='articles', through='articles.OriginalNews'),
        ),
    ]
