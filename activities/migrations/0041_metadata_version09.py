# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from activities.models import MetadataOption


def update_learning(*args, **kwargs):
    MetadataOption.objects.get(group='space_science', code='other').delete()


class Migration(migrations.Migration):
    dependencies = [
        ('activities', '0040_metadata_version09-update'),
    ]

    operations = [
        migrations.RunPython(update_learning),
    ]
