from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^profile/$',views.profile, name='profile'),
    	url(r'^register/$', views.register, name='register')

)
