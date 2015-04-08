from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker.views import home, search, addComment, viewComment



urlpatterns = patterns('',
        url(r'^home/$', home, name='home'),
        url(r'^home/search/$', search, name='search'),
        url(r'^addComment/$', addComment, name='addComment'),
        url(r'^viewComment/$', viewComment, name='viewComment'),


    	)
