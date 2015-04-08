from django import forms
from workout_tracker.models import Comment



class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ("content",)