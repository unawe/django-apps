# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


REPOSITORIES = {
    'Scientix': None,
    'OER': None,
    'TES': None,
}


def move_repo(apps, schema_editor):
    Repository = apps.get_model('activities', 'Repository')
    RepositoryEntry = apps.get_model('activities', 'RepositoryEntry')

    for name in REPOSITORIES.keys():
        repo = Repository(name=name)
        REPOSITORIES[name] = repo
        repo.save()

    for entry in RepositoryEntry.objects.all():
        entry.repo = REPOSITORIES.get(entry.repo0, None)
        entry.save()


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0008_auto_20160213_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='repositoryentry',
            options={'verbose_name_plural': 'repository entries'},
        ),
        migrations.RenameField(
            model_name='repositoryentry',
            old_name='repo',
            new_name='repo0',
        ),
        migrations.AddField(
            model_name='repositoryentry',
            name='repo',
            field=models.ForeignKey(blank=True, null=True, to='activities.Repository'),
        ),

        migrations.RunPython(move_repo),

        migrations.RemoveField(
            model_name='repositoryentry',
            name='repo0',
        ),
        migrations.AlterField(
            model_name='repositoryentry',
            name='repo',
            field=models.ForeignKey(to='activities.Repository', null=True),
        ),

    ]
