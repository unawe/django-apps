# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0033_metadata_version09-change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='group',
            field=models.ForeignKey(to='activities.MetadataOption', verbose_name='Group or individual activity', default=18, related_name='+'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='learning',
            field=models.ForeignKey(to='activities.MetadataOption', verbose_name='type of learning activity', help_text='Enquiry-based learning model', related_name='learning+'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='max_number_at_once',
            field=models.IntegerField(verbose_name='Maximum number of people at once'),
        ),
        migrations.AlterField(
            model_name='metadataoption',
            name='group',
            field=models.CharField(max_length=50, choices=[('age', 'Age'), ('level', 'Level'), ('time', 'Time'), ('group', 'Group'), ('supervised', 'Supervised'), ('cost', 'Cost per student'), ('location', 'Location'), ('skills', 'Core skills'), ('learning', 'Type(s) of learning activity'), ('content_area_focus', 'Content Area focus'), ('astronomical_scientific_category', 'Astronomical Scientific Categories'), ('earth_science_keyword', 'Earth Science keywords'), ('space_science_keyword', 'Space Science keywords')]),
        ),
    ]
