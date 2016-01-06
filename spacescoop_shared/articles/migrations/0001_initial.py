# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ArticleTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('language_code', models.CharField(db_index=True, verbose_name='Language', max_length=15)),
                ('title', models.CharField(max_length=255)),
                ('master', models.ForeignKey(editable=False, null=True, related_name='translations', to='articles.Article')),
            ],
            options={
                'managed': True,
                'db_tablespace': '',
                'db_table': 'articles_article_translation',
                'verbose_name': 'article Translation',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='articletranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
