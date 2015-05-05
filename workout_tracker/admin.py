from django.contrib import admin
from workout_tracker.models import Client
from workout_tracker.models import Trainer
from workout_tracker.models import Workout
from workout_tracker.models import Comment
from workout_tracker.models import Exercise
from .models import Notification

# Register your models here.
admin.site.register(Client)
admin.site.register(Trainer)
admin.site.register(Workout)
admin.site.register(Comment)
admin.site.register(Exercise)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'actor',
                    'level', 'target', 'unread', 'public')
    list_filter = ('level', 'unread', 'public', 'timestamp', )

admin.site.register(Notification, NotificationAdmin)