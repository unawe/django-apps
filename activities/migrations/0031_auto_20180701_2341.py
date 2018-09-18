# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0030_metadata_version09_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='astronomical_scientific_category',
            field=models.ManyToManyField(verbose_name='Astronomical Scientific Categories', related_name='_activity_astronomical_scientific_category_+', to='activities.MetadataOption'),
        ),
        migrations.AddField(
            model_name='activity',
            name='earth_science_keyword',
            field=models.ManyToManyField(verbose_name='Earth Science keywords', related_name='_activity_earth_science_keyword_+', to='activities.MetadataOption'),
        ),
        migrations.AddField(
            model_name='activity',
            name='space_science_keyword',
            field=models.ManyToManyField(verbose_name='Space Science keywords', related_name='_activity_space_science_keyword_+', to='activities.MetadataOption'),
        ),
        migrations.AlterField(
            model_name='metadataoption',
            name='group',
            field=models.CharField(choices=[('age', 'Age'), ('level', 'Level'), ('time', 'Time'), ('group', 'Group'), ('supervised', 'Supervised'), ('cost', 'Cost per student'), ('location', 'Location'), ('skills', 'Core skills'), ('learning', 'Type(s) of learning activity'), ('content_area_focus', 'Content Area focus'), ('specific_content_category', 'Specific Content Category')], max_length=50),
        ),
    ]
