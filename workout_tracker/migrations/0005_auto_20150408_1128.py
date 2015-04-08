# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0004_auto_20150407_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='client',
            field=models.ForeignKey(related_name='workout', blank=True, to='workout_tracker.Client', null=True),
            preserve_default=True,
        ),
    ]
