# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0039_metadata_version09-update'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='other_keyword',
            field=models.ManyToManyField(related_name='_activity_other_keyword_+', to='activities.MetadataOption', verbose_name='Other', blank=True),
        ),
    ]
