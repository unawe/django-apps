# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import migrations, models
import activities.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(null=True, auto_now_add=True)),
                ('modification_date', models.DateTimeField(null=True, auto_now=True)),
                ('lang', models.CharField(max_length=5, default='en')),
                ('code', models.CharField(unique=True, max_length=4, help_text='The 4 digit code that identifies the Activity, in the format "YY##": year, folowed by sequential number.')),
                ('slug', models.SlugField(unique=True, max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.')),
                ('uuid', models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)),
                ('doi', models.CharField(blank=True, max_length=50, verbose_name='DOI', help_text='Digital Object Identifier, in the format XXXX/YYYY. See http://www.doi.org/')),
                ('title', models.CharField(max_length=255, help_text='Title is shown in browser window. Use a good informative title, since search engines normally display the title on their result pages.', db_index=True)),
                ('teaser', models.TextField(max_length=140, help_text='One line, 140 characters maximum')),
                ('theme', models.CharField(max_length=40, help_text='Use top level AVM metadata')),
                ('keywords', models.TextField(help_text='List of keywords, separated by commas')),
                ('acknowledgement', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(verbose_name='brief description', help_text='Maximum 2 sentences! Maybe what and how?')),
                ('goals', models.TextField()),
                ('objectives', models.TextField(verbose_name='Learning Objectives')),
                ('evaluation', models.TextField(blank=True, help_text='If the teacher/educator wants to evaluate the impact of the activity, how can she/he do it?')),
                ('materials', models.TextField(blank=True, help_text='Please indicate costs and/or suppliers if possible')),
                ('background', models.TextField(verbose_name='Background Information')),
                ('fulldesc', models.TextField(verbose_name='Full Activity Description')),
                ('curriculum', models.TextField(blank=True, verbose_name='Connection to school curriculum', help_text='Please indicate which country')),
                ('additional_information', models.TextField(blank=True, help_text='Notes, Tips, Resources, Follow-up, Questions, Safety Requirements, Variations')),
                ('conclusion', models.TextField()),
            ],
            options={
                'ordering': ['-code'],
                'abstract': False,
                'verbose_name_plural': 'activities',
            },
        ),
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('file', models.FileField(blank=True, upload_to=activities.models.get_file_path_step)),
                ('main_visual', models.BooleanField(help_text='The main visual is used as the cover image.', default=False)),
                ('show', models.BooleanField(help_text='Include in attachment list.', verbose_name='Show', default=False)),
                ('position', models.PositiveSmallIntegerField(help_text='Used to define the order of attachments in the attachment list.', verbose_name='Position', default=0)),
                ('hostmodel', models.ForeignKey(to='activities.Activity')),
            ],
            options={
                'ordering': ['-show', 'position', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('citable_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AuthorInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('activity', models.ForeignKey(related_name='authors', to='activities.Activity')),
                ('author', models.ForeignKey(to='activities.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(null=True, auto_now_add=True)),
                ('modification_date', models.DateTimeField(null=True, auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, help_text='Slug identifies the Collection; it is used as part of the URL. Use only lowercase characters.')),
                ('description', models.TextField(blank=True, verbose_name='brief description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='collections')),
                ('activities', models.ManyToManyField(related_name='_collection_activities_+', to='activities.Activity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True, db_index=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField(blank=True, max_length=255)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='institutions')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='MetadataOption',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('group', models.CharField(choices=[('age', 'Age'), ('level', 'Level'), ('time', 'Time'), ('group', 'Group'), ('supervised', 'Supervised'), ('cost', 'Cost'), ('location', 'Location'), ('skills', 'Core skills'), ('learning', 'Type of learning activity')], max_length=50)),
                ('code', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('position', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'ordering': ['group', 'position'],
            },
        ),
        migrations.CreateModel(
            name='RepositoryEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('repo', models.CharField(max_length=50)),
                ('url', models.URLField(max_length=255)),
                ('activity', models.ForeignKey(to='activities.Activity')),
            ],
            options={
                'ordering': ['repo'],
                'verbose_name_plural': 'repository entries',
            },
        ),
        migrations.AlterUniqueTogether(
            name='metadataoption',
            unique_together=set([('group', 'code')]),
        ),
        migrations.AddField(
            model_name='authorinstitution',
            name='institution',
            field=models.ForeignKey(to='activities.Institution'),
        ),
        migrations.AddField(
            model_name='activity',
            name='age',
            field=models.ManyToManyField(related_name='_activity_age_+', to='activities.MetadataOption'),
        ),
        migrations.AddField(
            model_name='activity',
            name='cost',
            field=models.ForeignKey(null=True, to='activities.MetadataOption', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='activity',
            name='group',
            field=models.ForeignKey(null=True, to='activities.MetadataOption', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='activity',
            name='learning',
            field=models.ForeignKey(to='activities.MetadataOption', help_text='Enquiry-based learning model', related_name='+', verbose_name='type of learning activity'),
        ),
        migrations.AddField(
            model_name='activity',
            name='level',
            field=models.ManyToManyField(related_name='_activity_level_+', to='activities.MetadataOption', help_text='Specify at least one of "Age" and "Level". '),
        ),
        migrations.AddField(
            model_name='activity',
            name='location',
            field=models.ForeignKey(null=True, to='activities.MetadataOption', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='activity',
            name='skills',
            field=models.ManyToManyField(related_name='_activity_skills_+', to='activities.MetadataOption', verbose_name='core skills'),
        ),
        migrations.AddField(
            model_name='activity',
            name='supervised',
            field=models.ForeignKey(null=True, to='activities.MetadataOption', blank=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='activity',
            name='time',
            field=models.ForeignKey(related_name='+', to='activities.MetadataOption'),
        ),
    ]
