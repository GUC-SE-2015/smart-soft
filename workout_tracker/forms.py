from django.contrib.auth.models import User
from django import forms
from workout_tracker.models import user

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('name','username','gender','email','password','date_of_birth')

	#password = forms.CharField(widget=forms.PasswordInput())
 