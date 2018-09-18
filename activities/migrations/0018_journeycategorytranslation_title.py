# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0017_auto_20180406_0209'),
    ]

    operations = [
        migrations.AddField(
            model_name='journeycategorytranslation',
            name='title',
            field=models.CharField(default=1, verbose_name='Title', max_length=255),
            preserve_default=False,
        ),
    ]
