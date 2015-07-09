from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^home$', views.home_view, name='home'),
    url(r'^product/wine/(?P<wine_id>\d+)/$', views.wine_view, name='wine_view'),
    url(r'^list_wine/(?P<filter>[a-zA-Z]+)/(?P<value>[a-zA-Z]+)/$', views.list_wines_view, name='list_wine'),
    url(r'^add_wine_shopping$', views.add_wine_shopping, name='add_wine_shopping'),
    url(r'^search$', views.search, name='search'),
)