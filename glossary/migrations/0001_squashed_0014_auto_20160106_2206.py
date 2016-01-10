# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields
import autoslug.fields


class Migration(migrations.Migration):

    replaces = [('glossary', '0001_initial'), ('glossary', '0002_auto_20150917_1152'), ('glossary', '0003_auto_20150921_1522'), ('glossary', '0004_auto_20150921_1617'), ('glossary', '0005_remove_entrytranslation_slug'), ('glossary', '0006_auto_20150921_1634'), ('glossary', '0007_auto_20150927_2303'), ('glossary', '0008_auto_20150928_1727'), ('glossary', '0009_auto_20150928_1734'), ('glossary', '0010_auto_20151006_1430'), ('glossary', '0011_auto_20151013_1756'), ('glossary', '0012_auto_20151021_1709'), ('glossary', '0013_auto_20151203_1518'), ('glossary', '0014_auto_20160106_2206')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EntryTranslation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('slug', models.SlugField(help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.', max_length=255, unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('short_description', models.CharField(max_length=160, verbose_name='short description')),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('master', models.ForeignKey(to='glossary.Entry', related_name='translations', null=True, editable=False)),
            ],
            options={
                'db_table': 'glossary_entrytranslation',
                'managed': True,
                'verbose_name': 'entry Translation',
                'default_permissions': (),
                'db_tablespace': '',
            },
        ),
        migrations.AlterUniqueTogether(
            name='entrytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='short_description',
            field=ckeditor.fields.RichTextField(max_length=160, verbose_name='short description'),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='short_description',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterModelOptions(
            name='entrytranslation',
            options={},
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='master',
            field=models.ForeignKey(related_name='translations', null=True, to='glossary.Entry'),
        ),
        migrations.AlterModelTable(
            name='entrytranslation',
            table=None,
        ),
        migrations.RemoveField(
            model_name='entrytranslation',
            name='slug',
        ),
        migrations.AddField(
            model_name='entrytranslation',
            name='slug',
            field=models.SlugField(default='', max_length=255, help_text='The Slug must be unique, and closely match the title for better SEO; it is used as part of the URL.'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='entrytranslation',
            unique_together=set([('language_code', 'master'), ('language_code', 'slug')]),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique_with=('language_code',), always_update=True, populate_from='title', editable=False),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='entrytranslation',
            name='short_description',
            field=models.CharField(max_length=180),
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries', 'ordering': ['translations__title']},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries', 'ordering': ('translations__title',)},
        ),
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
    ]
