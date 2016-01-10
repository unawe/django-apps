# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0037_auto_20151203_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='originalnewssourcetranslation',
            options={'verbose_name': 'partner translation'},
        ),
        migrations.AlterField(
            model_name='originalnewssource',
            name='fullname',
            field=models.CharField(max_length=200, blank=True, help_text='If set, the full name will be used in some places instead of the name'),
        ),
    ]
