# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0015_auto_20170824_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='JourneyCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JourneyCategoryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('language_code', models.CharField(db_index=True, verbose_name='Language', max_length=15)),
                ('description', models.TextField(verbose_name='General introduction', blank=True)),
                ('master', models.ForeignKey(to='activities.JourneyCategory', null=True, related_name='translations')),
            ],
            options={
                'abstract': False,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='JourneyChapter',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(null=True, blank=True)),
                ('activities', models.ManyToManyField(to='activities.Activity', blank=True, related_name='_journeychapter_activities_+')),
                ('journey', models.ForeignKey(to='activities.JourneyCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='JourneyChapterTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('language_code', models.CharField(db_index=True, verbose_name='Language', max_length=15)),
                ('title', models.CharField(verbose_name='Chapter title', max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(verbose_name='Chapter introduction', blank=True)),
                ('master', models.ForeignKey(to='activities.JourneyChapter', null=True, related_name='translations')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='journeychaptertranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
