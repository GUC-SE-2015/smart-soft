from django.contrib import admin
from workout_tracker.models import Client
from workout_tracker.models import Trainer
from workout_tracker.models import Workout
#from workout_tracker.models import *
from workout_tracker.models import Comment
from workout_tracker.models import Exercise

# Register your models here.


admin.site.register(Trainer)
admin.site.register(Client)
#admin.site.register(Comment)
admin.site.register(Workout)
admin.site.register(Comment)
admin.site.register(Exercise)

