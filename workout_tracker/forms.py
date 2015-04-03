from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from workout_tracker.models import Trainer, Client, UserInfo

class TrainerUserForm(forms.ModelForm):
	class Meta:
		model = Trainer
		exclude = ['user', 'type']

class ClientUserForm(forms.ModelForm):
	class Meta:
		model = Client
		exclude = ['user', 'type', 'trainer']


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user        

"""class CustomUserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('first name','last name','gender','email','password','date_of_birth')        
"""

"""class UserSignUpForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email'].strip()
        try:
            User.objects.get(email__iexact=email)
            raise forms.ValidationError('email already exists')
        except User.DoesNotExist:
            return email

    def clean_password1(self):
        pw1 = self.cleaned_data.get('password')
        pw2 = self.cleaned_data.get('password1')
        if pw1 and pw2 and pw1 == pw2:
            return pw2
        raise forms.ValidationError("passwords don't match")

    def save(self, commit=True):
        user = super(UserSignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user    
"""


    



 