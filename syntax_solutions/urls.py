<<<<<<< HEAD
=======

>>>>>>> 9a41923216453c50f5426034aa16079b659cce88
from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker import views

urlpatterns = patterns('',
<<<<<<< HEAD
    # Examples:
=======
  
>>>>>>> 9a41923216453c50f5426034aa16079b659cce88
    # url(r'^$', 'syntax_solutions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^$', include('workout_tracker.urls')),
	url(r'^workout_tracker/', include('workout_tracker.urls')),
    #url(r'^register/', views.register, name='register'),

)
 
=======
    #url(r'^$', 'workout_tracker.views.show'),
    url(r'^my_clients/$', views.view_clients),
    url(r'^search/$', views.search),

    url(r'^', include('workout_tracker.urls')),

   )
>>>>>>> 9a41923216453c50f5426034aa16079b659cce88
