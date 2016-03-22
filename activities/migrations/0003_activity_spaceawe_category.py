# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0002_auto_20160120_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='spaceawe_category',
            field=models.CharField(choices=[('space', 'Space Exploration'), ('planet', 'Earth Observation'), ('nav', 'Navigation'), ('herit', 'Islamic heritage')], max_length=20, blank=True),
        ),
    ]
