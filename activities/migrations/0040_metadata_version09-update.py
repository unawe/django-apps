# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from activities.models import MetadataOption


def add(group, code, title, position):
    x = MetadataOption(group=group, code=code, title=title, position=position)
    x.save()


def update_learning(*args, **kwargs):
    i = 0
    i += 1; add('other', 'other', 'Other', i)

class Migration(migrations.Migration):
    dependencies = [
        ('activities', '0040_activity_other_keyword'),
    ]

    operations = [
        migrations.RunPython(update_learning),
    ]
