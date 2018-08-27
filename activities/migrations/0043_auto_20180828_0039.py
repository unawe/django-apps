# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0042_auto_20180828_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='link',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
