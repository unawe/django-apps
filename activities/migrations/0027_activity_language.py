# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0026_activity_original_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='language',
            field=models.CharField(default='English', max_length=64),
            preserve_default=False,
        ),
    ]
