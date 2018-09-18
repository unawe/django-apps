# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0006_auto_20160213_1552'),
        ('activities', '0025_auto_20180701_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='original_author',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Original Author of the activity (if not the authors listed above', to='institutions.Person'),
        ),
    ]
