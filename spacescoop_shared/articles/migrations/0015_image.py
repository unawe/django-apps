# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
# import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        # ('filer', '0002_auto_20150606_2003'),
        ('articles', '0014_originalnewssource_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('main_visual', models.BooleanField(help_text='The main visual is used as the cover image.', default=False)),
                ('show', models.BooleanField(help_text='Include in attachment list.', default=False, verbose_name='Show')),
                ('position', models.PositiveSmallIntegerField(help_text='Used to define the order of attachments in the attachment list.', default=0, verbose_name='Position')),
                # ('file', filer.fields.image.FilerImageField(related_name='article_image', null=True, blank=True, to='filer.Image')),
                ('hostmodel', models.ForeignKey(to='articles.Article')),
            ],
            options={
                'abstract': False,
                'ordering': ['-show', 'position', 'id'],
            },
        ),
    ]
