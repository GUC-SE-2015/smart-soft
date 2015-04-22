# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='myImg',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Profile Pic', blank=True),
            preserve_default=True,
        ),
    ]
