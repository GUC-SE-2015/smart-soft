from django.shortcuts import render, render_to_response
from django.template import RequestContext
from friendship.models import Friend, Follow
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from workout_tracker.forms import TrainerUserForm, ClientUserForm, UserCreateForm, WorkoutForm, ExerciseForm
from models import Trainer, Client, User, UserInfo, Workout, Exercise
from friendship.models import FriendshipRequest
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



#Done by : Eric Philippe issue #38
def view_trainer(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    return render(request,'trainer_home.html', {
        "trainer":trainer,
        "owner": False if request.user.is_anonymous() else request.user.user_info.id == trainer.id})

#Done by : Eric Philippe issue #38
def view_trainer_info(request, trainer_id):
	#view trainer profile 
    trainer = Trainer.objects.get(id=trainer_id)
    return render(request,'profile_trainer.html', {
        "trainer":trainer,
        "owner": False if request.user.is_anonymous() else request.user.user_info.id == trainer.id})


def view_client(request, client_id):
    client = Client.objects.get(id=client_id)
    return render(request,'client_home.html', {
        "client":client,
        "owner": False if request.user.is_anonymous() else request.user.user_info.id == client.id})
    
def view_client_info(request, client_id):
	#view client profile
    client = Client.objects.get(id=client_id)
    return render(request,'profile_client.html', {
        "client":client,
        "owner": False if request.user.is_anonymous() else request.user.user_info.id == client.id})


def trainers(request):
    return render(request,'trainers.html', {"trainers":Trainer.objects.all()})    


def clients(request):
    return render(request,'clients.html', {"clients":Client.objects.all()})    


def provide_trainer_info(request, user=None, register=False):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if not register and request.method =='POST' :
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user = User.objects.get(pk=request.POST['user_id'])
        trainer = Trainer(user=user)
        trainer_form = TrainerUserForm(request.POST, instance=trainer)
        ##################################################profile_form = userForm(data=request.POST)

        # If the two forms are valid...
        if trainer_form.is_valid():
            trainer1 = trainer_form.save(commit=False)
            trainer1.type = 'trainer'
            # Save the user's form data to the database.
            trainer1.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return view_trainer(request, user.user_info.id)
            #current_user=Trainer.objects.get(id=request.user.id)
            #return render_to_response('trainer_profile.html', {'current_user': current_user}, context)
            #return render(request, 'trainer_profile.html', {'trainer': current_user.id }) 
            #return view_trainer(request, user_info.id)


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
            {'trainer_form': trainer_form, 'user':user, 'registered': registered},
            context)    


def provide_client_info(request, user=None, register=False):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if not register and request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user = User.objects.get(pk=request.POST['user_id'])
        client = Client(user=user)
        client_form = ClientUserForm(request.POST, instance=client)

        # If the two forms are valid...
        if client_form.is_valid():
            # Save the user's form data to the database.
            client1 = client_form.save(commit=False)
            client1.type = 'client'
            client1.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return view_client(request, user.user_info.id)

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
            {'client_form': client_form, 'user':user, 'registered': registered},
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
                user_info = request.user.user_info
                if user_info.type == 'client':
                    return view_client(request, user_info.id)
                else:
                    return view_trainer(request, user_info.id)

                # return render_to_response('Homepage.html', {}, context)
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
        
        if request.user.is_anonymous():
            return render_to_response('login.html', {}, context)
        else:
            print "USER:", request.user.first_name
            user_info = request.user.user_info
            if user_info.type == 'trainer':
                return view_trainer(request, user_info.id)
            else:
                return view_client(request, user_info.id) 


def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login')         


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
        user_form = UserCreateForm(data=request.POST)
        ##################################################profile_form = userForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Update our variable to tell the template registration was successful.
            registered = True

            if request.POST.get("trainer"):
                #redirect to trainer form
                return provide_trainer_info(request, user=user, register=True)
                
            else:
                #redirect to client form
                return provide_client_info(request, user=user, register=True)
                
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserCreateForm
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


def create_follow_request(request, tid):
    user = User.objects.get(pk=tid)
    new_relationship = Friend.objects.add_friend(request.user, user)
    return view_trainer_info(request, user.user_info.id)
    # Can optionally save a message when creating friend requests
    message_relationship = Friend.objects.add_friend(
        from_user=request.user,
        to_user= some_other_user,
        message='Hi, I would like to follow you',
    )

def accept(request, pid):
    FriendshipRequest.objects.get(id=pid).accept()
    user_info = request.user.user_info
    return view_trainer(request,user_info.id)


def reject(request, pid):
    FriendshipRequest.objects.get(id=pid).reject()
    user_info = request.user.user_info
    return view_trainer(request,user_info.id)


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
    return user_login(request)


def homepage(request):
    return render(request,'Homepage.html')


def data(request):
    User.objects.all().delete()

    user = User.objects.create_superuser(
        'admin',
        'alexan.nader@gmail.com', 'pass')
    user.first_name = 'Nader'
    user.last_name = 'Alexan'
    user.save()
    trainer = Trainer(
        user=user,
        date_of_birth='1994-1-1',
        gender='Male',
        type='trainer',
        phone='01005577997',
        experience='so much experience, so much wow',
        education='Saint Fatima el Sele7dar High School'
        )
    trainer.save()
    
    user = User.objects.create_superuser('mirna',
        'mirna@gmail.com', 'pass')
    user.first_name = 'Mirna'
    user.last_name = 'Benjamin'
    user.save()
    client = Client(
        user=user,
        date_of_birth='1994-1-1',
        gender='Female',
        type='client',
        health_issues='All work best, very very awesome, quite tiny',
        weight=40.0,
        height=120.0,
        )
    client.save()
    return trainers(request)


def schedule_trainer(request,client_id):
    client_workout = Client.objects.get(id=client_id).workout.all()
    return render(request,'client_schedule.html', {'client_workout': client_workout, 'client_id': client_id})

def schedule_client(request):
    client_workout = request.user.user_info.client.workout.all()
    return render(request,'client_schedule.html', {'client_workout': client_workout})


#Done By: Noha Gomaa Issue: #43 Url:/add_workout
def add_workout(request):
     # Like before, get the request's context.
    context = RequestContext(request)
    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        workout_form = WorkoutForm(data=request.POST)
        # If the two form is valid...
        if workout_form.is_valid():
            # Save the user's form data to the database.
            workout = workout_form.save(commit=False)
            workout.posted_by = request.user
            workout.client = request.user.user_info.client
            workout.save()
            return add_exercise(request, workout_id= workout.id)
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print workout_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        workout_form = WorkoutForm()

    # Render the template depending on the context.
    return render_to_response('add_workout.html',{'workout_form': workout_form},context)

#Done By: Noha Gomaa Issue: #43 Url:/add_workout_trainer
def add_workout_trainer(request, client_id):
    # Like before, get the request's context.
    context = RequestContext(request)

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        workout_form = WorkoutForm(data=request.POST)
        # If the form is valid...
        if workout_form.is_valid():
            # Save the user's form data to the database.
            workout = workout_form.save(commit=False)
            workout.posted_by = request.user
            workout.client = Client.objects.get(id = client_id) 
            workout.save()
            return add_exercise(request, workout_id= workout.id)
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print workout_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        workout_form = WorkoutForm()

    # Render the template depending on the context.
    return render_to_response('add_workout.html',{'workout_form': workout_form , 'client_id': client_id},context)          

#Done By: Noha Gomaa Issue: #43 Url:/add_exercise
def add_exercise(request, workout_id ):

        # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method =='POST' :
        # Attempt to grab information from the raw form information.
        exercise_form = ExerciseForm(data=request.POST)

        # If the two forms are valid...
        if exercise_form.is_valid():
            # Save the user's form data to the database.
            exercise = exercise_form.save(commit=False)
            exercise.workout = Workout.objects.get(pk=workout_id)
            exercise.save()
            return HttpResponseRedirect('/add_exercise/%s' % workout_id ) 
            


            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        #else:
            #print user_form.errors
    else:
        exercise_form = ExerciseForm()
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    #else:
        #user_form = CustomUserForm()
        ##################################################profile_form = userForm()

    # Render the template depending on the context.
    return render_to_response(
            'add_exercise.html',
            {'exercise_form': exercise_form,
            'workout_id': workout_id,
            },
            context)    

#Done By: Noha Gomaa Issue: #44 Url:/workout_done
def mark_done(request, workout_id):
    
    workout = request.user.user_info.client.workout.get(id=workout_id)
    workout.done = True  
    workout.save()
    return schedule_client(request)

"""def view_exercise_trainer(request, workout_id ):
    client_exercise = request.user.user_info.client.workout.get(id=workout_id)
    exercise = client_exercise.exercise.all()
    return render(request,'exercise.html', {'exercise':exercise, 'workout_id': workout_id} )"""

#Done By: Seif Keshk Issue:#37 Url:/view_exercise
def view_exercise(request, workout_id):
    #Grab selected workout from schedule
    workout =  Workout.objects.get(id = workout_id)
    u2= request.user.user_info.type
    #Get all exercises belonging to this workout
    exercise = workout.exercise.all()
    return render(request,'exercise.html', {'exercise':exercise, 'workout': workout, 'u2':u2} )

    #Done by Mirna Benyamine #41(show statistics) url:/stat


def stat(request):
    user = request.user
    #to get all the workout of the loged client.
    x=len(Workout.objects.filter(client=user.user_info))
    #to get the done workouts of the loged client.
    y=len(Workout.objects.filter(done=True, client=user.user_info))
    print "y: ", y
    if x != 0:
        print "here"
    #to calculate the % of the workouts done.    
        result = 100*y/x
        return render(request,'stat.html',{'result':result})
    else:
        result = 0
    return render(request,'stat.html',{'result':result})

#Done by Mirna Benyamine #42(edit profile) url:/update
def update (request, u_id):
# to get the information of the loged user.    
    u=User.objects.filter(id=u_id)
    u2=UserInfo.objects.filter(user=u)
 #to return the html where the user will edit his information.   
    return render_to_response('update.html', {'u':u, 'u2': u2}, context_instance=RequestContext(request)) 
    
#Done by Mirna Benyamine #42(edit profile) url:/edit_info        
def edit_info(request, u_id):
    user = request.user
    user_info = user.user_info
#this will appear to both clients and trainers
    if request.POST:
      user.first_name = request.POST['firstname']
      user.last_name = request.POST['lastname']
      user.save()
      user.set_password(request.POST['newpassword'])

#if the loged user is a trainer, this extra information will appear to be edited
      if user_info.type == 'trainer':
        user_info = user.user_info
        user_info.phone = request.POST['phone']
        user_info.experience = request.POST['experience']
        user_info.education = request.POST['education']
        user_info.save()
#it will then return the updated trainer profile.
        return HttpResponseRedirect('/logout')  

      else:  
#else if the loged user is a client, this extra information will appear to be edited 
        user.health_issues = request.POST['health_issues']
        user.save()
        user.weight = request.POST['weight'] 
        user.save()
        user.height = request.POST['height']
        user.save()
#then it will retuen the updated client profile.
      return HttpResponseRedirect('/logout') 

    else: 
      return render_to_response('update.html',{'u':user, 'u2':user_info}, context_instance=RequestContext(request))