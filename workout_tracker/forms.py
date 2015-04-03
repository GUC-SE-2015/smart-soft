from django.contrib.auth.models import User
from django import forms
from workout_tracker.models import Trainer, Client

class TrainerUserForm(forms.ModelForm):
	class Meta:
		model = Trainer
		exclude = ['user']

class ClientUserForm(forms.ModelForm):
	class Meta:
		model = Client
		exclude = ['user']




    



 