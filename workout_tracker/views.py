from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from friendship.models import Friend, Follow
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def my_view(request):
    # List of this user's friends
    all_friends = Friend.objects.friends(request.user)

    # List all unread friendship requests
    requests = Friend.objects.unread_requests(user=request.user)

    # List all rejected friendship requests
    rejects = Friend.objects.rejected_requests(user=request.user)

    # Count of all rejected friendship requests
    reject_count = Friend.objects.rejected_request_count(user=request.user)

    # List all unrejected friendship requests
    unrejects = Friend.objects.unrejected_requests(user=request.user)

    # Count of all unrejected friendship requests
    unreject_count = Friend.objects.unrejected_request_count(user=request.user)

    # List all sent friendship requests
    sent = Friend.objects.sent_requests(user=request.user)

    # List of this user's followers
    all_followers = Following.objects.followers(request.user)

    # List of who this user is following
    following = Following.objects.following(request.user)

    ### Managing friendship relationships

    # Create a friendship request
    other_user = User.objects.get(pk=1)
    new_relationship = Friend.objects.add_friend(request.user, other_user)

    # Can optionally save a message when creating friend requests
    message_relationship = Friend.objects.add_friend(
        from_user=request.user,
        to_user=some_other_user,
        message='Hi, I would like to be your friend',
    )

    # And immediately accept it, normally you would give this option to the user
    new_relationship.accept()

    # Now the users are friends
    Friend.objects.are_friends(request.user, other_user) == True

    # Remove the friendship
    Friend.objects.remove_friend(other_user, request.user)

    # Create request.user follows other_user relationship
    following_created = Following.objects.add_follower(request.user, other_user)

def show(request):
	if not User.objects.all():
		first_user = User.objects.create_superuser('Noha','noha-gomaa@gmail.com','pass')
		first_user.save()
		sec_user = User.objects.create_user('Soad','noha-g@gmail.com','pass')
		sec_user.save()
		new_relationship = Friend.objects.add_friend(first_user, sec_user)
		new_relationship.accept()
	#friends.objects
	return render_to_response('friends.html', {}, context_instance=RequestContext(request))
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
                return HttpResponseRedirect('/workout/')
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
        return render_to_response('workout-tracker/login.html', {}, context)
