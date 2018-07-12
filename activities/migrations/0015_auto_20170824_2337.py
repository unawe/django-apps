# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0014_languageattachment_languageattachmenttranslation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='activities',
            field=models.ManyToManyField(blank=True, related_name='collections', to='activities.Activity'),
        ),
    ]
