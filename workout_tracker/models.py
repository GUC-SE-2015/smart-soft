
from django.db import models
from django.contrib.auth.models import User


GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male'),
        )
USER_TYPE_CHOICES = (
    ('trainer', 'trainer'),
    ('client', 'client'),
    )

class UserInfo(models.Model):
    user = models.OneToOneField(User, related_name='user_info')
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    type = models.CharField(max_length=256, choices=USER_TYPE_CHOICES)

    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
    

class Trainer(UserInfo):
    phone = models.CharField(max_length=30)
    experience = models.TextField()
    education = models.TextField()


class Client(UserInfo):
    trainer = models.ForeignKey(Trainer, related_name='clients', null=True, blank=True)
    health_issues = models.TextField()
    weight = models.FloatField()
    height = models.FloatField()
