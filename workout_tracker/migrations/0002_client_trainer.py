# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='workout_tracker.user')),
                ('health_issues', models.CharField(max_length=2000)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
            ],
            options={
            },
            bases=('workout_tracker.user',),
        ),
        migrations.CreateModel(
            name='trainer',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='workout_tracker.user')),
                ('phone', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=2000)),
                ('education', models.CharField(max_length=2000)),
            ],
            options={
            },
            bases=('workout_tracker.user',),
        ),
    ]
