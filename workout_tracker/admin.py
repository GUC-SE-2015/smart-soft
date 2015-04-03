from django.contrib import admin
from workout_tracker.models import Client
from workout_tracker.models import Trainer

# Register your models here.
admin.site.register(Client)
admin.site.register(Trainer)