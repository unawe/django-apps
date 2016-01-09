# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import spacescoop_shared.articles.models
import sorl.thumbnail.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0039_auto_20160109_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name='image',
            name='file',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=spacescoop_shared.articles.models.get_file_path_article_attachment, blank=True),
        ),
        migrations.AddField(
            model_name='originalnewssource',
            name='logo',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='partners', blank=True),
        ),
    ]
