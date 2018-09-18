# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0028_auto_20180701_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytranslation',
            name='further_reading',
            field=models.TextField(verbose_name='Further reading', blank=True, default=''),
        ),
    ]
