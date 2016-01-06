# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0036_auto_20151119_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='originalnewssource',
            name='fullname',
            field=models.CharField(max_length=200, help_text='If set, the full name will be used in some places instead of the name'),
        ),
        migrations.AlterField(
            model_name='originalnewssource',
            name='name',
            field=models.CharField(max_length=200, help_text='Short (and commonly used) name', unique=True),
        ),
        migrations.AlterField(
            model_name='originalnewssourcetranslation',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, help_text='Text to appear in Parnet page'),
        ),
    ]
