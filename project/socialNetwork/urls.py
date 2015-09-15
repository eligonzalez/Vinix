from django.conf.urls import patterns, url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns(
    '',
    url(r'^profile/(?P<idUser>\d+)/$', views.profile, name='profile'),
    url(r'^followers', views.followers, name='followers'),
    url(r'^home_social', views.home_social, name='home_social'),
    url(r'^remove_followers/(?P<follower>\d+)/(?P<followed>\d+)/$', views.remove_followers, name='remove_followers'),
    url(r'^add_followers/(?P<follower>\d+)/(?P<followed>\d+)/$', views.add_followers, name='add_followers'),
    url(r'^search_people$', views.search_people, name='search_people'),
    url(r'^search_wine$', views.search_wine, name='search_wine'),
    url(r'^add_post$', views.add_post, name='add_post'),
    url(r'^remove_post/(?P<idPost>\d+)/(?P<idUser>\d+)/$', views.remove_post, name='remove_post'),
    url(r'^wines_social', views.wines_social, name='wines_social'),
    url(r'^add_favorite_product/(?P<idProduct>\d+)/$', views.add_favorite_product, name='add_favorite_product'),
    url(r'^remove_favorite_product/(?P<idProduct>\d+)/$', views.remove_favorite_product, name='remove_favorite_product'),
    url(r'^home2', views.home2, name='imageupload'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)