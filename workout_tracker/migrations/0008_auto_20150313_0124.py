# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0007_auto_20150313_0124'),
    ]

    operations = [
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
    ]
