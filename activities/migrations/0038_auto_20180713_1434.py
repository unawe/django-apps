# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0037_metadata_version09-update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='learning',
        ),
        migrations.AddField(
            model_name='activity',
            name='learning',
            field=models.ManyToManyField(to='activities.MetadataOption', verbose_name='type of learning activity', related_name='_activity_learning_+', help_text='Enquiry-based learning model'),
        ),
    ]
