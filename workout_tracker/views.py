from django.shortcuts import render
from django.template import RequestContext
from workout_tracker.forms import CustomUserForm
from django.shortcuts import render_to_response
from workout_tracker.models import user

# Create your views here.
def index(request):
    return render(request, 'workout_tracker/index.html')

def profile(request, ):
    """Edit user profile."""
    profile = user.objects.get(user=1)
    img = None

    if request.method == "POST":
        pf = ProfileForm(request.POST, request.FILES, instance=profile)
        if pf.is_valid():
            pf.save()
            imfn = pjoin(MEDIA_ROOT, profile.avatar.name)
            im = PImage.open(imfn)
            im.thumbnail((160,160), PImage.ANTIALIAS)
            im.save(imfn, "JPEG")
    else:
        pf = ProfileForm(instance=profile)

    if profile.myImg:
        img = "/media/" + profile.myImg.name
    return render_to_response("forum/profile.html", add_csrf(request, pf=pf, img=img))


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


