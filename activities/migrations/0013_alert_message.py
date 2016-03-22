# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def init_alert_message(apps, schema_editor):
    Activity = apps.get_model("activities", "Activity")
    ActivityTranslation = apps.get_model("activities", "ActivityTranslation")
    for activity in Activity.objects.all():
        activity_t = ActivityTranslation.objects.get(master=activity, language_code='en')
        activity_t.alert_message = u'Stay tuned - This resource will soon be available in: French, Dutch, Spanish, Italian, German, Greek, Portuguese, and Polish'
        activity_t.save()


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0012_activitytranslation_spaceawe_authorship'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitytranslation',
            name='alert_message',
            field=models.TextField(blank=True, help_text='Alert message, do display at the top of the activity page'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='theme',
            field=models.CharField(max_length=40, help_text='Use top level AVM metadata'),
        ),
        migrations.AlterField(
            model_name='activitytranslation',
            name='spaceawe_authorship',
            field=models.TextField(blank=True, verbose_name='Space Awareness authorship'),
        ),

        migrations.RunPython(init_alert_message),

    ]
