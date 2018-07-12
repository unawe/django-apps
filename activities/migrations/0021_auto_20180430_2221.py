# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0020_auto_20180411_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journeychapter',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='journeychapter',
            name='position',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
