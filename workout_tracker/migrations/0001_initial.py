# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('commenter', models.ForeignKey(related_name='commenter', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
                ('count', models.PositiveIntegerField()),
                ('lap', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('type', models.CharField(max_length=256, choices=[(b'trainer', b'trainer'), (b'client', b'client')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('userinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='workout_tracker.UserInfo')),
                ('phone', models.CharField(max_length=30)),
                ('experience', models.TextField()),
                ('education', models.TextField()),
            ],
            options={
            },
            bases=('workout_tracker.userinfo',),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('userinfo_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='workout_tracker.UserInfo')),
                ('health_issues', models.TextField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('trainer', models.ForeignKey(related_name='clients', blank=True, to='workout_tracker.Trainer', null=True)),
            ],
            options={
            },
            bases=('workout_tracker.userinfo',),
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, choices=[(b'Arm', b'Arm'), (b'Legs', b'Legs'), (b'Deltoids', b'Deltoids'), (b'Chest', b'Chest'), (b'Back', b'Back'), (b'Fitness', b'Fitness')])),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('done', models.NullBooleanField()),
                ('client', models.ForeignKey(related_name='workout', to='workout_tracker.Client')),
                ('posted_by', models.ForeignKey(related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(related_name='user_info', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='exercise',
            name='workout',
            field=models.ForeignKey(related_name='exercise', to='workout_tracker.Workout'),
            preserve_default=True,
        ),
    ]
