from django.db import models

# Create your models here.
class user (models.Model):
	name = models.CharField(max_length=100)
	date_of_birth = models.DateField()
	Genders= (
        ('F', 'Female'),
        ('M', 'Male'),
        )
	gender = models.CharField(max_length=1, choices=Genders)
	email = models.CharField(max_length=50)

class client(user):
	health_issues = models.CharField(max_length=2000)
	weight = models.FloatField()
	height = models.FloatField()

class trainer(user):
    phone = models.CharField(max_length=30)
    experience = models.CharField(max_length=2000)
    education = models.CharField(max_length=2000)




