# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0027_activity_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='age',
            field=models.ManyToManyField(verbose_name='Age range', to='activities.MetadataOption', related_name='_activity_age_+'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='cost',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='activities.MetadataOption', verbose_name='Cost per student'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='group',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='activities.MetadataOption', verbose_name='Group or individual activity'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='level',
            field=models.ManyToManyField(verbose_name='Education level', to='activities.MetadataOption', related_name='_activity_level_+', help_text='Specify at least one of "Age" and "Level". '),
        ),
        migrations.AlterField(
            model_name='activity',
            name='supervised',
            field=models.ForeignKey(blank=True, null=True, related_name='+', to='activities.MetadataOption', verbose_name='Supervised for safety'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='further_reading',
            field=models.TextField(blank=True, verbose_name='Further reading'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='reference',
            field=models.TextField(blank=True, verbose_name='References'),
        ),
    ]
