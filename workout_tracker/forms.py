from django.contrib.auth.models import User
from django import forms
from workout_tracker.models import user

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ('name','username','gender','email','password')



class ProfileForm(forms.ModelForm):
    class Meta:
        model = user
        field=('myImg')
	#password = forms.CharField(widget=forms.PasswordInput())
