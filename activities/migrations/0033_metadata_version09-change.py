# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from activities.models import MetadataOption


def add(group, code, title, position):
    x = MetadataOption.objects.create(group=group, code=code, title=title, position=position)
    x.save()


def add_new_values(*args, **kwargs):
    i = MetadataOption.objects.filter(group='time').aggregate(models.Max('position'))['position__max']
    i += 1; add('time', '3-6h', '3-6h', i)
    i += 1; add('time', '6-24h', '6-24h', i)
    i += 1; add('time', 'multiple_days', 'multiple days', i)
    i += 1; add('time', 'week', 'a week', i)
    i += 1; add('time', 'many_weeks', 'over many weeks', i)
    i += 1; add('time', 'many_months', 'over many months', i)
    i += 1; add('time', 'year_longer', 'a year or longer', i)

    i = MetadataOption.objects.filter(group='learning').aggregate(models.Max('position'))['position__max']
    i += 1; add('learning', 'guided_discovery_learning', 'Guided-discovery learning', i)
    i += 1; add('learning', 'structured_inquiry_learning', 'Structured-inquiry learning', i)
    i += 1; add('learning', 'interactive_lecture', 'Interactive Lecture', i)
    i += 1; add('learning', 'lecture_demonstration', 'Lecture Demonstration', i)
    i += 1; add('learning', 'student_teaching', 'Student Teaching', i)
    i += 1; add('learning', 'problem_solving', 'Problem-solving', i)
    i += 1; add('learning', 'project_based_learning', 'Project-based learning', i)
    i += 1; add('learning', 'self_and_peer_assessment', 'Self and Peer Assessment', i)
    i += 1; add('learning', 'student_presentation', 'Student Presentation', i)
    i += 1; add('learning', 'reading_watching_comprehension', 'Reading/Watching Comprehension', i)
    i += 1; add('learning', 'technology_based', 'Technology-based', i)
    i += 1; add('learning', 'role_playing_drama_performance', 'Role-Playing/Drama/Performance', i)
    i += 1; add('learning', 'creative_expression', 'Creative Expression', i)
    i += 1; add('learning', 'debate', 'Debate', i)
    i += 1; add('learning', 'discussion_groups', 'Discussion Groups', i)
    i += 1; add('learning', 'teacher_directed_socratic_dialogue', 'Teacher Directed Socratic Dialogue', i)
    i += 1; add('learning', 'game_mediated_learning', 'Game-mediated learning', i)
    i += 1; add('learning', 'puzzle_based_learning', 'Puzzle-based learning', i)
    i += 1; add('learning', 'fun_activity', 'Fun activity', i)
    i += 1; add('learning', 'social_research', 'Social Research', i)
    i += 1; add('learning', 'modelling', 'Modelling', i)
    i += 1; add('learning', 'traditional_science_experiment', 'Traditional Science Experiment', i)
    i += 1; add('learning', 'media_focussed_learning', 'Media-focussed Learning', i)
    i += 1; add('learning', 'historical_focussed_activity', 'Historical focussed activity', i)
    i += 1; add('learning', 'assessment_technique', 'Assessment Technique', i)
    i += 1; add('learning', 'informal_field_trip_related', 'Informal/Field Trip Related', i)
    i += 1; add('learning', 'case_study', 'Case Study', i)
    i += 1; add('learning', 'direct_instruction', 'Direct Instruction', i)
    i += 1; add('learning', 'drill_and_practice', 'Drill and Practice', i)
    i += 1; add('learning', 'simulation_focussed', 'Simulation focussed', i)
    i += 1; add('learning', 'fine_art_focussed', 'Fine Art focussed', i)
    i += 1; add('learning', 'observation_based', 'Observation based', i)
    i += 1; add('learning', 'reflective_practice_blogs,_journals', 'Reflective practice (blogs, journals)', i)
    i += 1; add('learning', 'other', 'Other', i)


def delete_old(*args, **kwargs):
    # delete all learning
    learning = MetadataOption.objects.filter(group='learning')
    for l in learning:
        l.code = 'obsolete_' + l.code
        l.save()


def update_level(*args, **kwargs):
    MetadataOption.objects.filter(group='level', title="Primary School").update(title="Primary")
    MetadataOption.objects.filter(group='level', title="Secondary School").update(title="Secondary")
    m = MetadataOption.objects.filter(group='level').aggregate(models.Max('position'))['position__max']
    add('level', 'other', 'Other', m+1)


def update_cost(*args, **kwargs):
    add('cost', 'free', 'Free', 0)
    MetadataOption.objects.filter(group='cost', code="low").update(title="Low Cost", position=2)
    MetadataOption.objects.filter(group='cost', code="average").update(title="Medium Cost", position=3)
    MetadataOption.objects.filter(group='cost', code="expensive").update(title="High Cost", position=4)


def update_location(*arg, **kwargs):
    MetadataOption.objects.filter(group='location', code="indoors_small").update(title="Small Indoor Setting (e.g. classroom)")
    MetadataOption.objects.filter(group='location', code="indoors_large").update(title="Large Indoor Setting (e.g. school hall)")
    m = MetadataOption.objects.filter(group='location').aggregate(models.Max('position'))['position__max']
    add('location', 'computer_laboratory', 'Computer Laboratory', m + 1)
    add('location', 'science_laboratory', 'Science Laboratory', m + 2)
    add('location', 'does_not_matter', 'Does not matter', m + 3)


def update_supervised(*arg, **kwargs):
    MetadataOption.objects.filter(group='supervised', code="supervised").update(title="Yes")
    MetadataOption.objects.filter(group='supervised', code="unsupervised").update(title="No")

class Migration(migrations.Migration):
    dependencies = [
        ('activities', '0032_auto_20180701_2354'),
    ]

    operations = [
        migrations.RunPython(delete_old),
        migrations.RunPython(add_new_values),
        migrations.RunPython(update_level),
        migrations.RunPython(update_cost),
        migrations.RunPython(update_location),
        migrations.RunPython(update_supervised)
    ]
