from django.contrib import admin
from workout_tracker.models import Client
from workout_tracker.models import Trainer
from workout_tracker.models import Workout

# Register your models here.
admin.site.register(Client)
admin.site.register(Trainer)
admin.site.register(Workout)
