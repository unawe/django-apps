# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0011_big_idea_translatable'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitytranslation',
            name='spaceawe_authorship',
            field=models.TextField(blank=True, verbose_name='Space Awareness authorship', max_length=200),
        ),
    ]
