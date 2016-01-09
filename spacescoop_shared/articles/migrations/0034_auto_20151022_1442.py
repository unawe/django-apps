# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
# import filer.fields.image
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0033_originalnewssource_article_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='originalnewssource',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='name', editable=False, default=''),
            preserve_default=False,
        ),
        # migrations.AlterField(
        #     model_name='image',
        #     name='file',
        #     field=filer.fields.image.FilerImageField(related_name='+', to='filer.Image', blank=True, null=True),
        # ),
        # migrations.AlterField(
        #     model_name='originalnewssource',
        #     name='logo',
        #     field=filer.fields.image.FilerImageField(related_name='+', to='filer.Image', blank=True, null=True),
        # ),
        migrations.AlterField(
            model_name='originalnewssource',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
