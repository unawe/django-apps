# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0006_auto_20160213_1552'),
        ('activities', '0022_auto_20180430_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='affiliation',
            field=models.CharField(default='version9', verbose_name='Affiliation or organisation', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='country',
            field=models.ForeignKey(to='institutions.Location', default=1, verbose_name='Country(s)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='email',
            field=models.CharField(default='version9', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='max_number_at_once',
            field=models.IntegerField(default=0, verbose_name='Maximum number of people at one'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='suitable_group_size',
            field=models.IntegerField(default=0, verbose_name='Suitable group size'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitytranslation',
            name='further_reading',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitytranslation',
            name='reference',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='activitytranslation',
            name='short_desc_material',
            field=models.TextField(blank=True, verbose_name='Short description of Suplementary material'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='evaluation',
            field=models.TextField(help_text='If the teacher/educator wants to evaluate the impact of the activity, how can she/he do it?'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='fulldesc',
            field=models.TextField(verbose_name='Full description of the activity'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='materials',
            field=models.TextField(blank=True, help_text='Please indicate costs and/or suppliers if possible', verbose_name='List of material'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='teaser',
            field=models.TextField(help_text='250 words', verbose_name='Abstract', max_length=140),
        ),
        migrations.AlterField(
            model_name='metadataoption',
            name='group',
            field=models.CharField(choices=[('age', 'Age'), ('level', 'Level'), ('time', 'Time'), ('group', 'Group'), ('supervised', 'Supervised'), ('cost', 'Cost per student'), ('location', 'Location'), ('skills', 'Core skills'), ('learning', 'Type of learning activity'), ('content_area_focus', 'Content Area focus')], max_length=50),
        ),
    ]
