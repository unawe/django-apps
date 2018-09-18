# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0043_auto_20180828_0039'),
    ]

    operations = [
        migrations.AddField(
            model_name='linktranslation',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
