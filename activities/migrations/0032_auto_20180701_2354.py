# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0031_auto_20180701_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='content_area_focus',
            field=models.ManyToManyField(verbose_name='Content Area focus', related_name='_activity_content_area_focus_+', to='activities.MetadataOption'),
        ),
        migrations.AlterField(
            model_name='metadataoption',
            name='group',
            field=models.CharField(max_length=50, choices=[('age', 'Age'), ('level', 'Level'), ('time', 'Time'), ('group', 'Group'), ('supervised', 'Supervised'), ('cost', 'Cost per student'), ('location', 'Location'), ('skills', 'Core skills'), ('learning', 'Type(s) of learning activity'), ('content_area_focus', 'Content Area focus'), ('astronomical_scientific_category', 'Astronomical Scientific Categories'), ('earth_science', 'Earth Science keywords'), ('space_science', 'Space Science keywords')]),
        ),
    ]
