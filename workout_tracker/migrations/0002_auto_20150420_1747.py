# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date_posted',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
