# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='trainer',
            field=models.ForeignKey(related_name='clients', default=0, blank=True, to='workout_tracker.Trainer'),
            preserve_default=False,
        ),
    ]
