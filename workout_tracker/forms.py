from django.contrib.auth.models import User
from django import forms
from workout_tracker.models import MyUser, Trainer, Client

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('name','username','gender','email','password', 'date_of_birth')
        widgets = {
            'password': forms.PasswordInput(),
        }

class TrainerUserForm(forms.ModelForm):
	class Meta:
		model = Trainer
		exclude = ['user']

class ClientUserForm(forms.ModelForm):
	class Meta:
		model = Client
		exclude = ['user', 'trainer']


 