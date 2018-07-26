# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from activities.models import MetadataOption


def add(group, code, title, position):
    x = MetadataOption(group=group, code=code, title=title, position=position)
    x.save()


def update_learning(*args, **kwargs):
    m = MetadataOption.objects.filter(group='learning').aggregate(models.Max('position'))['position__max']
    other = MetadataOption.objects.get(group='learning', code='other')
    position = other.position
    other.position = m + 1
    other.save()
    add('learning', 'fun_activity', 'Fun activity', position)

class Migration(migrations.Migration):
    dependencies = [
        ('activities', '0038_auto_20180713_1434'),
    ]

    operations = [
        migrations.RunPython(update_learning),
    ]
