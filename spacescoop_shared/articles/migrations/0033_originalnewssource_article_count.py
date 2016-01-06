# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0032_auto_20151021_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='originalnewssource',
            name='article_count',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
