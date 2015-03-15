# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('workout_tracker', '0003_auto_20150312_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myuser',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=1, choices=[(b'F', b'Female'), (b'M', b'Male')])),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.RemoveField(
            model_name='client',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='client',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='gender',
        ),
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(related_name='client', to='workout_tracker.Myuser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(related_name='trainer', to='workout_tracker.Myuser'),
            preserve_default=True,
        ),
    ]
