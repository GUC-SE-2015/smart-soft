from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
    	url(r'^register/$', views.register, name='register')
	    url(r'^pending_requests/$', views.view_pending),
	    url(r'^my_clients/$', views.view_clients),
	    url(r'^trainer_profile/$',views.view_trainerprofile),
)
