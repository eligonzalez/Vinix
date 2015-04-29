from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.home, name='home'),
    url(r'^login$', views.login_view, name='login'),
    url(r'^loginf$', views.login_form, name='loginf'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^register$', views.register, name='register'),
    url(r'^users/(?P<username>\w+)/$', views.profiler, name="profiler"),
    url(r'^follow/(?P<follow>\w+)/$', views.add_follower, name='follow'),
    url(r'^unfollow/(?P<follow>\w+)/$', views.remove_follower, name='unfollow'),
)