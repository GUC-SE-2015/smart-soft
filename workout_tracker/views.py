from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from workout_tracker.forms import CommentForm
from .models import Trainer , Comment

def search(request):
  if request.GET:
    query=request.GET['query']
    result = Trainer.objects.none()
    for q in query.split(' '):
      result |= Trainer.objects.filter(user__first_name__icontains=q)
    print 'result', result

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


def addComment(request):

  context = RequestContext(request)
  if request.method == 'POST':
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
            # Save the user's form data to the database
        Comment = comment_form.save()
        return render_to_response ('addComments.html',{'comment_form': comment_form}, context)
    else:
      print comment_form.errors
  else:
      comment_form = CommentForm
      return render_to_response('addComments.html',{'comment_form':comment_form}, context)


def viewComment(request):
  comment = Comment.objects.all()
  return render(request,'viewComments.html',{})    

