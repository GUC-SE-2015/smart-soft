# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workout_tracker', '0003_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workout', models.TextField()),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('client', models.ForeignKey(related_name='client', blank=True, to='workout_tracker.Client', null=True)),
                ('posted_by', models.ForeignKey(related_name='user', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='workouts',
            name='client',
        ),
        migrations.RemoveField(
            model_name='workouts',
            name='posted_by',
        ),
        migrations.DeleteModel(
            name='Workouts',
        ),
    ]
