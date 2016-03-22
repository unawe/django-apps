# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def copy_en_fields(apps, schema_editor):
    Activity = apps.get_model("activities", "Activity")
    ActivityTranslation = apps.get_model("activities", "ActivityTranslation")
    for activity in Activity.objects.all():
        activity_t = ActivityTranslation.objects.get(master=activity, language_code='en')
        activity_t.big_idea = activity.big_idea
        activity_t.save()


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0010_auto_20160303_1104'),
    ]

    operations = [

        migrations.AddField(
            model_name='activitytranslation',
            name='big_idea',
            field=models.CharField(blank=True, max_length=200, verbose_name='Big Idea of Science'),
        ),

        migrations.RunPython(copy_en_fields),

        migrations.RemoveField(
            model_name='activity',
            name='big_idea',
        ),

    ]
