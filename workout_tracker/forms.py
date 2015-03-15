from django.contrib.auth.models import User
from django import forms
from workout_tracker.models import MyUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('name','username','gender','email','password','date_of_birth')

	#password = forms.CharField(widget=forms.PasswordInput())
 