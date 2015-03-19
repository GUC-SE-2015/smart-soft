# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0002_myuser_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(related_name='client', to='workout_tracker.MyUser'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(related_name='trainer', to='workout_tracker.MyUser'),
            preserve_default=True,
        ),
    ]
