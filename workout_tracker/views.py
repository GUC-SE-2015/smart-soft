from django.shortcuts import render

def view_trainerprofile(request):
      #user = request.User.trainer     
    user = {
      "name":"Ronnie Coleman",
      "email":"Coleman@gmail.com",
      "phone":"0123456789",
      "experience": "10 years working as a trainer",
     }
    
    return render(request,'trainer_profile.html', {"user":user})

def view_clientprofile(request):
    user = {
    "name":"keshk",
    "email":"keshk@gmail.com",
    "phone":"0123456789",
    "height": "170 CM",
    "weight":"67 KG",

    }
    
    return render(request,'client_profile.html',{"user":user})

def data(request):
    User.object.all().delete()
    user= MyUser(date_of_birth= '1994-1-1', gender='Female', username= 'bino', email= 'bino@gmail.com')
# Create your views here.

