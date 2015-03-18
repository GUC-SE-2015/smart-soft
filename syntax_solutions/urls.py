from django.conf.urls import patterns, include, url
from django.contrib import admin
from workout_tracker.views import home, search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'syntax_solutions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', home),
    url(r'^home/search/$', search, name='search'),

)
