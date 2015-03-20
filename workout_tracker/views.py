from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext

# Create your views here.
from models import Trainer

def search(request):
  if request.GET:
    query=request.GET['query']
    result = Trainer.objects.none()
    for q in query.split(' '):
      result |= Trainer.objects.filter(user__first_name__icontains=q)

  return HttpResponse([r.user.username for r in result])


      

def home(request):
  return render_to_response('home.html', {}, context_instance=RequestContext(request))

  


def data(request):
  Trainer.object.delete.all()
  user = User(date_of_birth='1994-1-1',gender='Female')
  trainer = Trainer(user=user, experience='lalalala',phone='01010108090',education='hahahahha')
  user= User(date_of_birth='1993-3-12',gender='Male')
  trainer = Trainer(user=user,phone='012387363',experience='lelelelle',education='hehehehehe')
  return HttpResponse('sucess')
