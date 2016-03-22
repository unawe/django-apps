# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0005_auto_20160125_0507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='big_idea',
            field=models.CharField(max_length=200, blank=True, verbose_name='Big Idea of Science'),
        ),
    ]
