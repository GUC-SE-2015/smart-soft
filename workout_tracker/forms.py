from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from workout_tracker.models import Trainer, Client, UserInfo, Workout, Comment

<<<<<<< HEAD


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ("content",)


=======
>>>>>>> 330ac7f3a51388f786d8ddc32e56f346cbdee9ce
class TrainerUserForm(forms.ModelForm):
	class Meta:
		model = Trainer
		exclude = ['user', 'type']

<<<<<<< HEAD

=======
>>>>>>> 330ac7f3a51388f786d8ddc32e56f346cbdee9ce
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

<<<<<<< HEAD

=======
>>>>>>> 330ac7f3a51388f786d8ddc32e56f346cbdee9ce
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ("workout", "due_date")






    



<<<<<<< HEAD
 

=======
 
>>>>>>> 330ac7f3a51388f786d8ddc32e56f346cbdee9ce
