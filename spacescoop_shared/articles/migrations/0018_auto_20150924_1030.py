# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20150921_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('language_code', models.CharField(verbose_name='Language', db_index=True, max_length=15)),
                ('slug', models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=255)),
                ('title', models.CharField(verbose_name='title', max_length=255)),
                ('master', models.ForeignKey(null=True, to='articles.Category', related_name='translations')),
            ],
        ),
        migrations.AlterModelOptions(
            name='articletranslation',
            options={},
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='master',
            field=models.ForeignKey(null=True, to='articles.Article', related_name='translations'),
        ),
        migrations.AlterField(
            model_name='articletranslation',
            name='slug',
            field=models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'master')]),
        ),
        migrations.AlterModelTable(
            name='articletranslation',
            table=None,
        ),
        migrations.AlterUniqueTogether(
            name='categorytranslation',
            unique_together=set([('language_code', 'slug'), ('language_code', 'master')]),
        ),
    ]
