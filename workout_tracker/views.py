from django.shortcuts import render

def view_trainerprofile(request):
	user = {
	  "name":"seif",
	  "email":"seif@gmail.com"
	 }

	return render(request, 'trainer_profile.html', {"user":user})
# Create your views here.

