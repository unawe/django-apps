# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0034_auto_20180702_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='cost',
            field=models.ForeignKey(related_name='+', verbose_name='Cost per student', to='activities.MetadataOption', default=226),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=models.ForeignKey(related_name='+', to='activities.MetadataOption', default=229),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='supervised',
            field=models.ForeignKey(related_name='+', verbose_name='Supervised for safety', to='activities.MetadataOption', default=20),
            preserve_default=False,
        ),
    ]
