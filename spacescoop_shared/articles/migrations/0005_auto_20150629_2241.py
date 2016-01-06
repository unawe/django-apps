# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20150629_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='A',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=4, help_text='The 4 digit code that identifies the Activity, in the format "YY##": year, folowed by sequential number.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ATranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('master', models.ForeignKey(null=True, editable=False, related_name='translations', to='articles.A')),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'db_table': 'articles_a_translation',
                'default_permissions': (),
                'verbose_name': 'a Translation',
            },
        ),
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=4, help_text='The 4 digit code that identifies the Activity, in the format "YY##": year, folowed by sequential number.')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='C',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(null=True, auto_now_add=True)),
                ('modification_date', models.DateTimeField(null=True, auto_now=True)),
                ('code', models.CharField(max_length=4, help_text='The 4 digit code that identifies the Activity, in the format "YY##": year, folowed by sequential number.')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='D',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('featured', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('release_date', models.DateTimeField()),
                ('embargo_date', models.DateTimeField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(null=True, auto_now_add=True)),
                ('modification_date', models.DateTimeField(null=True, auto_now=True)),
                ('code', models.CharField(max_length=4, help_text='The 4 digit code that identifies the Activity, in the format "YY##": year, folowed by sequential number.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('master', models.ForeignKey(null=True, editable=False, related_name='translations', to='articles.D')),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'db_table': 'articles_d_translation',
                'default_permissions': (),
                'verbose_name': 'd Translation',
            },
        ),
        migrations.AlterUniqueTogether(
            name='dtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='atranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
