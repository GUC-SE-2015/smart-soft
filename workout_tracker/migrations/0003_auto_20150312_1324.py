# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0002_auto_20150312_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='trainer',
            field=models.ForeignKey(related_name='clients', blank=True, to='workout_tracker.Trainer', null=True),
            preserve_default=True,
        ),
    ]
