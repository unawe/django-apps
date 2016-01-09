# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0038_auto_20160106_2206'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attachment',
        ),
    ]
