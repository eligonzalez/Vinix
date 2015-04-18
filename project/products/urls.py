from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^home$', views.home_view, name='home'),
    url(r'^product/wine/(?P<wine_id>\d+)/$', views.wine_view, name='wine_view'),
)