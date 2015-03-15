# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('workout_tracker', '0004_auto_20150312_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(related_name='client', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='trainer',
            name='user',
            field=models.OneToOneField(related_name='trainer', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
