# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0024_auto_20180701_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='email',
            field=models.CharField(max_length=64, verbose_name='Email address of corresponding author'),
        ),
    ]
