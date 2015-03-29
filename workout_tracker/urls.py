from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker import views

urlpatterns = patterns('',
    
        url(r'^$', views.index, name='index'),
    	url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
    	url(r'^register/(?P<user_type>.+)/$', views.register),
    	url(r'^trainer_info/$', views.provide_trainer_info, name='provide_trainer_info'),
    	url(r'^client_info/$', views.provide_client_info, name='provide_client_info'),
        url(r'^homepage/$', views.homepage, name='homepage'),
    	url(r'^view_pending/$', views.view_pending, name='view_pending'),
    	url(r'^accept/(?P<pid>\d+)$', views.accept, name='accept'),
    	url(r'^reject/(?P<pid>\d+)$', views.reject, name='reject'),
        url(r'^trainer_profile/$',views.view_trainerprofile, name='trainer_profile'),
        url(r'^client_profile/$',views.view_clientprofile, name='client_profile'),
        url(r'^client_workouts/$',views.schedule, name='client_workouts'),
        #url(r'^client_profile/client_workouts/$',views.schedule, name='client_Pworkouts'),
    	
    	url(r'^data/$', views.data, name='data'),
)
