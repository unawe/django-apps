# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0030_auto_20151006_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(db_index=True, help_text='The 4 digit code that identifies the Article, in the format "YY##": year, folowed by sequential number.', max_length=4),
        ),
    ]
