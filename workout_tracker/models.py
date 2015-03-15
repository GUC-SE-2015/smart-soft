
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Myuser (User):
    
    date_of_birth = models.DateField()
    Genders= (
        ('F', 'Female'),
        ('M', 'Male'),
        )
    gender = models.CharField(max_length=1, choices=Genders)

class Trainer(models.Model):
    user = models.OneToOneField(User, related_name='trainer')
    phone = models.CharField(max_length=30)
    experience = models.CharField(max_length=2000)
    education = models.CharField(max_length=2000)


class Client(models.Model):
    user = models.OneToOneField(User, related_name='client')
    trainer = models.ForeignKey(Trainer, related_name='clients', null=True, blank=True)
    health_issues = models.CharField(max_length=2000)
    weight = models.FloatField()
    height = models.FloatField()






