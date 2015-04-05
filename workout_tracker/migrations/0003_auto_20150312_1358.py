# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0002_client_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'123456', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=b'xxxxxx', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='workout_tracker.user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='user_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='workout_tracker.user'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=75),
            preserve_default=True,
        ),
    ]