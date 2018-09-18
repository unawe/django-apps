# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0023_auto_20180701_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitytranslation',
            name='title',
            field=models.CharField(db_index=True, max_length=255, help_text='Title is shown in browser window. Use a good informative title, since search engines normally display the title on their result pages.', verbose_name='Activity title'),
        ),
    ]
