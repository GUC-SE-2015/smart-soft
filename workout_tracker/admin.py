from django.contrib import admin
from workout_tracker.models import Client
from workout_tracker.models import Trainer
from workout_tracker.models import Workout
from workout_tracker.models import *

# Register your models here.


admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(Comment)
admin.site.register(Workout)
