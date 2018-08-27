# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0041_metadata_version09'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('type', models.IntegerField(choices=[(0, 'Other'), (1, 'Video')], default=0)),
                ('main', models.BooleanField(default=False)),
                ('activity', models.ForeignKey(to='activities.Activity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LinkTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('language_code', models.CharField(max_length=15, db_index=True, verbose_name='Language')),
                ('title', models.CharField(blank=True, max_length=64)),
                ('url', models.CharField(max_length=255)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='activities.Link')),
            ],
        ),
        migrations.AlterField(
            model_name='collectiontranslation',
            name='slug',
            field=models.SlugField(help_text='Slug identifies the Collection; it is used as part of the URL.', unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='activitytranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='linktranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
