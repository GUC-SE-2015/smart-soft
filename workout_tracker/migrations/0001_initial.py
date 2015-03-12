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
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('health_issues', models.CharField(max_length=2000)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
                ('phone', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=2000)),
                ('education', models.CharField(max_length=2000)),
                ('user', models.OneToOneField(related_name='trainer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='client',
            name='trainer',
            field=models.ForeignKey(related_name='clients', blank=True, to='workout_tracker.Trainer', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(related_name='client', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
