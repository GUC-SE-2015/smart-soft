from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from workout_tracker.forms import CustomUserForm, TrainerUserForm, ClientUserForm
from models import Trainer, MyUser
from friendship.models import FriendshipRequest
from django.contrib.auth import logout 


def view_trainerprofile(request):
    user = {
      "name":"seif",
      "email":"seif@gmail.com"
     }

    return render(request, 'trainer_profile.html', {"user":user})


def provide_trainer_info(request, user=None, register=False):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if not register and request.POST:
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        trainer_form = TrainerUserForm(request.POST)
        ##################################################profile_form = userForm(data=request.POST)

        # If the two forms are valid...
        if trainer_form.is_valid():
            # Save the user's form data to the database.
            user = trainer_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            #user.set_password(user.password)
            #user.save()

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
        #else:
            #print user_form.errors
    else:
        trainer_form = TrainerUserForm(initial={'user':user})
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    #else:
        #user_form = CustomUserForm()
        ##################################################profile_form = userForm()

    # Render the template depending on the context.
    return render_to_response(
            'trainer_info.html',
            {'trainer_form': trainer_form, 'registered': registered},
            context)    

def provide_client_info(request, user=None, register=False):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if not register and request.POST:
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        client_form = ClientUserForm(request.POST)
        ##################################################profile_form = userForm(data=request.POST)

        # If the two forms are valid...
        if client_form.is_valid():
            # Save the user's form data to the database.
            user = client_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            #user.set_password(user.password)
            #user.save()

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
        #else:
            #print user_form.errors
    else:
        client_form = ClientUserForm(initial={'user':user})
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    #else:
        #user_form = CustomUserForm()
        ##################################################profile_form = userForm()

    # Render the template depending on the context.
    return render_to_response(
            'client_info.html',
            {'client_form': client_form},
            context)                                               



def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return render_to_response('Homepage.html', {}, context)
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your workout account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)


def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')         



def register(request, user_type=None):
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

            if user_type == 'trainer':
                #redirect to trainer form
                return provide_trainer_info(request, user=user, register=True)
                
            else:
                #redirect to client form
                return provide_client_info(request, user=user, register=True)
                
            # assume the user is a trainer


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

def accept(request, pid):
    FriendshipRequest.objects.get(id=pid).accept()
    return HttpResponse('friend accepted')

def reject(request, pid):
    FriendshipRequest.objects.get(id=pid).reject()
    return HttpResponse('friend rejected')

def search(request):
  if request.GET:
    query=request.GET['query']
    result = Trainer.objects.none()
    for q in query.split(' '):
      result |= Trainer.objects.filter(user__name__icontains=q)

  return HttpResponse([r.user.username for r in result])

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


def index(request):
    return render(request, 'workout_tracker/index.html')


def homepage(request):
	return render(request,'Homepage.html')


def data(request):
    User.objects.all().delete()

    user = MyUser(date_of_birth='1994-1-1',gender='Female', username='admin', email='alexan.nader@gmail.com')
    user.set_password('pass')
    user.is_staff = True
    user.is_superuser = True
    user.save()


    user1 = MyUser(date_of_birth='1994-1-1',gender='Female', username='Noha', email='noha.nader@gmail.com')
    user1.set_password('pass')
    user1.save()

    trainer = Trainer(user=user1, experience='lalalala',phone='01010108090',education='hahahahha')
    trainer.save()

    user2= MyUser(date_of_birth='1993-3-12',gender='Male', username='Seif', email='seif.nader@gmail.com')
    user2.set_password('pass')
    user2.save()

    trainer = Trainer(user=user2,phone='012387363',experience='lelelelle',education='hehehehehe')
    trainer.save()

    FriendshipRequest(from_user=user1, to_user=user).save()
    return HttpResponse('sucess')
