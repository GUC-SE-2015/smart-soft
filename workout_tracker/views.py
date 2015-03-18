from django.shortcuts import render

def view_trainerprofile(request):
      #user = request.User.trainer     
    user = {
      "name":"seif",
      "email":"seif@gmail.com"
     }
    
    return render(request,'trainer_profile.html', {"user":user})

def view_clientprofile(request):
    user = {
    "name":"keshk",
    "email":"keshk@gmail.com"
    }
    
    return render(request,'client_profile.html',{"user":user})

def data(request):
    User.object.all().delete()
    user= MyUser(date_of_birth= '1994-1-1', gender='Female', username= 'bino', email= 'bino@gmail.com')
# Create your views here.

