
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from workout_tracker.forms import CustomUserForm
from django.http import HttpResponse
from models import Trainer



def view_clients(request):
    all_friends = Friend.objects.friends(request.user)
    return render(request, 'friends.html', {'all_friends': all_friends})

def view_pending(request):
    unrejects = Friend.objects.unrejected_requests(user=request.user)
    return render(request, 'pending_follow_requests.html', {'unrejects': unrejects})

def create_follow_request(request):
    other_user = User.objects.get(pk=1)
    new_relationship = Friend.objects.add_friend(request.user, other_user)

    # Can optionally save a message when creating friend requests
    message_relationship = Friend.objects.add_friend(
        from_user=request.user,
        to_user=some_other_user,
        message='Hi, I would like to be your friend',
    )

def accept_request(request):
    new_relationship.accept()
    Friend.objects.are_friends(request.user, other_user) == True

def reject_request(request):
    new_relationship.reject()
    Friend.objects.are_friends(request.user, other_user) == False



#def my_view(request):
    # List of this user's friends
    #all_friends = Friend.objects.friends(request.user)

    # List all unread friendship requests
    #requests = Friend.objects.unread_requests(user=request.user)

    # List all rejected friendship requests
    #rejects = Friend.objects.rejected_requests(user=request.user)

    # Count of all rejected friendship requests
    #reject_count = Friend.objects.rejected_request_count(user=request.user)

    # List all unrejected friendship requests
    #unrejects = Friend.objects.unrejected_requests(user=request.user)

    # Count of all unrejected friendship requests
    #unreject_count = Friend.objects.unrejected_request_count(user=request.user)

    # List all sent friendship requests
    #sent = Friend.objects.sent_requests(user=request.user)

    # List of this user's followers
    #all_followers = Following.objects.followers(request.user)

    # List of who this user is following
    #following = Following.objects.following(request.user)

    ### Managing friendship relationships

    # Create a friendship request
""" other_user = User.objects.get(pk=1)
    new_relationship = Friend.objects.add_friend(request.user, other_user)

    # Can optionally save a message when creating friend requests
    message_relationship = Friend.objects.add_friend(
        from_user=request.user,
        to_user=some_other_user,
        message='Hi, I would like to be your friend',
    ) """

    # And immediately accept it, normally you would give this option to the user
    #new_relationship.accept()

    # Now the users are friends
    #Friend.objects.are_friends(request.user, other_user) == True

    # Remove the friendship
    #Friend.objects.remove_friend(other_user, request.user)

    # Create request.user follows other_user relationship
    #following_created = Following.objects.add_follower(request.user, other_user)

def show(request):
    if not User.objects.all():
        first_user = User.objects.create_superuser('Noha','noha-gomaa@gmail.com','pass')
        first_user.save()
        sec_user = User.objects.create_user('Soad','noha-g@gmail.com','pass')
        sec_user.save()
        new_relationship = Friend.objects.add_friend(first_user, sec_user)
        new_relationship.accept()

    first_user = User.objects.get(pk=1)

    return render_to_response('friends.html', {"user":first_user}, context_instance=RequestContext(request))

def view_trainerprofile(request):
	user = {
	  "name":"seif",
	  "email":"seif@gmail.com"
	 }

	return render(request, 'trainer_profile.html', {"user":user})
# Create your views here.
def index(request):
    return render(request, 'workout_tracker/index.html')



def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = CustomUserForm(data=request.POST)
        ##################################################profile_form = userForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            ##################################################profile = profile_form.save(commit=False)
            ##################################################profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            ##################################################if 'picture' in request.FILES:
                ##################################################profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            ##################################################profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = CustomUserForm()
        ##################################################profile_form = userForm()

    # Render the template depending on the context.
    return render_to_response(
            'workout_tracker/register.html',
            {'user_form': user_form,  'registered': registered},
            context)    	    	 	   



def search(request):
  if request.GET:
    query=request.GET['query']
    result = Trainer.objects.none()
    for q in query.split(' '):
      result |= Trainer.objects.filter(user__name__icontains=q)

  return HttpResponse([r.user.username for r in result])
      



def data(request):
  Trainer.object.delete.all()
  user = User(date_of_birth='1994-1-1',gender='Female')
  trainer = Trainer(user=user, experience='lalalala',phone='01010108090',education='hahahahha')
  user= User(date_of_birth='1993-3-12',gender='Male')
  trainer = Trainer(user=user,phone='012387363',experience='lelelelle',education='hehehehehe')
  return HttpResponse('sucess')


