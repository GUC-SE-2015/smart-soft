
from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'syntax_solutions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'workout_tracker.views.show'),
    url(r'^$', include('workout_tracker.urls')),
	url(r'^workout_tracker/', include('workout_tracker.urls')),

    #url(r'^register/', views.register, name='register'),

)

