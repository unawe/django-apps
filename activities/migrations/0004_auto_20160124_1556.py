# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0003_activity_spaceawe_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', max_length=200)),
                ('title', models.CharField(db_index=True, max_length=255, help_text='Title is shown in browser window. Use a good informative title, since search engines normally display the title on their result pages.')),
                ('teaser', models.TextField(max_length=140, help_text='One line, 140 characters maximum')),
                ('theme', models.CharField(max_length=40, help_text='Use top level AVM metadata')),
                ('keywords', models.TextField(help_text='List of keywords, separated by commas')),
                ('acknowledgement', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(verbose_name='brief description', help_text='Maximum 2 sentences! Maybe what and how?')),
                ('goals', models.TextField()),
                ('objectives', models.TextField(verbose_name='Learning Objectives')),
                ('evaluation', models.TextField(help_text='If the teacher/educator wants to evaluate the impact of the activity, how can she/he do it?', blank=True)),
                ('materials', models.TextField(help_text='Please indicate costs and/or suppliers if possible', blank=True)),
                ('background', models.TextField(verbose_name='Background Information')),
                ('fulldesc', models.TextField(verbose_name='Full Activity Description')),
                ('curriculum', models.TextField(help_text='Please indicate which country', verbose_name='Connection to school curriculum', blank=True)),
                ('additional_information', models.TextField(help_text='Notes, Tips, Resources, Follow-up, Questions, Safety Requirements, Variations', blank=True)),
                ('conclusion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CollectionTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='title', max_length=200)),
                ('description', models.TextField(verbose_name='brief description', blank=True)),
            ],
            options={
                'default_permissions': (),
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='activity',
            name='acknowledgement',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='additional_information',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='background',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='conclusion',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='curriculum',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='description',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='evaluation',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='fulldesc',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='objectives',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='teaser',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='title',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='description',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='title',
        ),
        migrations.AlterField(
            model_name='activity',
            name='spaceawe_category',
            field=models.CharField(help_text='Category for Space Awareness website', choices=[('space', 'Space Exploration'), ('planet', 'Earth Observation'), ('nav', 'Navigation'), ('herit', 'Islamic heritage')], max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='authorinstitution',
            name='author',
            field=models.ForeignKey(to='institutions.Person'),
        ),
        migrations.AlterField(
            model_name='authorinstitution',
            name='institution',
            field=models.ForeignKey(to='institutions.Institution'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='collections', blank=True),
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Institution',
        ),
        migrations.AddField(
            model_name='collectiontranslation',
            name='master',
            field=models.ForeignKey(to='activities.Collection', related_name='translations', null=True),
        ),
        migrations.AddField(
            model_name='activitytranslation',
            name='master',
            field=models.ForeignKey(to='activities.Activity', related_name='translations', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='activitytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
