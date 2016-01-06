# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0031_auto_20151014_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalNewsSourceTranslation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('master', models.ForeignKey(null=True, related_name='translations', to='articles.OriginalNewsSource')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='originalnewssourcetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
