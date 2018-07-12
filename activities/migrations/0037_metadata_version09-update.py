# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from activities.models import MetadataOption


def add(group, code, title, position):
    x = MetadataOption(group=group, code=code, title=title, position=position)
    x.save()


def update_learning(*args, **kwargs):
    MetadataOption.objects.filter(group='learning', code__in=('obsolete_demonstration', 'obsolete_fun', 'obsolete_full', 'obsolete_partial', 'fun_activity')).delete()
    MetadataOption.objects.filter(group='time', code='12h').delete()
    m = MetadataOption.objects.filter(group='space_science').aggregate(models.Max('position'))['position__max']
    add('space_science', 'other', 'Other', m + 1)

class Migration(migrations.Migration):
    dependencies = [
        ('activities', '0036_auto_20180712_1419'),
    ]

    operations = [
        migrations.RunPython(update_learning),
    ]
