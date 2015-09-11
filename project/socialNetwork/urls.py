from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^profile/(?P<idUser>\d+)/$', views.profile, name='profile'),
    url(r'^followers', views.followers, name='followers'),
    url(r'^home', views.home, name='home'),
    url(r'^remove_followers/(?P<follower>\d+)/(?P<followed>\d+)/$', views.remove_followers, name='remove_followers'),
    url(r'^add_followers/(?P<follower>\d+)/(?P<followed>\d+)/$', views.add_followers, name='add_followers'),
    url(r'^search_people$', views.search_people, name='search_people'),
    url(r'^add_post$', views.add_post, name='add_post'),
    url(r'^remove_post/(?P<idPost>\d+)/(?P<idUser>\d+)/$', views.remove_post, name='remove_post'),
)