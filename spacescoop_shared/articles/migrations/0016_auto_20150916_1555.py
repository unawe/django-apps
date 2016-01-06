# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attachment',
            options={'ordering': ['position', 'id']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position', 'id']},
        ),
        migrations.RemoveField(
            model_name='attachment',
            name='main_visual',
        ),
        migrations.RemoveField(
            model_name='image',
            name='main_visual',
        ),
    ]
