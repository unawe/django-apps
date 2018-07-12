# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0035_auto_20180702_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='astronomical_scientific_category',
            field=models.ManyToManyField(verbose_name='Astronomical Scientific Categories', related_name='_activity_astronomical_scientific_category_+', to='activities.MetadataOption', blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='earth_science_keyword',
            field=models.ManyToManyField(verbose_name='Earth Science keywords', related_name='_activity_earth_science_keyword_+', to='activities.MetadataOption', blank=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='learning',
            field=models.ForeignKey(to='activities.MetadataOption', help_text='Enquiry-based learning model', related_name='learning+', on_delete=django.db.models.deletion.SET_NULL, null=True, verbose_name='type of learning activity'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='space_science_keyword',
            field=models.ManyToManyField(verbose_name='Space Science keywords', related_name='_activity_space_science_keyword_+', to='activities.MetadataOption', blank=True),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='description',
            field=models.TextField(verbose_name='brief description', help_text='Maximum 2 sentences! Maybe what and how?', blank=True),
        ),
    ]
