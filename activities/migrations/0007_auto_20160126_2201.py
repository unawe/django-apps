# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0006_auto_20160125_0555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='spaceawe_category',
        ),
        migrations.AddField(
            model_name='activity',
            name='earth',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='heritage',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='navigation',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activity',
            name='space',
            field=models.BooleanField(default=False),
        ),
    ]
