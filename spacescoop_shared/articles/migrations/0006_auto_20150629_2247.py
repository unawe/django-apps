# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20150629_2241'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='atranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='atranslation',
            name='master',
        ),
        migrations.DeleteModel(
            name='B',
        ),
        migrations.DeleteModel(
            name='C',
        ),
        migrations.AlterUniqueTogether(
            name='dtranslation',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='dtranslation',
            name='master',
        ),
        migrations.DeleteModel(
            name='A',
        ),
        migrations.DeleteModel(
            name='ATranslation',
        ),
        migrations.DeleteModel(
            name='D',
        ),
        migrations.DeleteModel(
            name='DTranslation',
        ),
    ]
