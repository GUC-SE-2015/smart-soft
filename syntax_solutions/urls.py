
from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker import views

urlpatterns = patterns('',
  
    # url(r'^$', 'syntax_solutions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'workout_tracker.views.show'),
    url(r'^my_clients/$', views.view_clients),
    url(r'^search/$', views.search),

    url(r'^', include('workout_tracker.urls')),

   )