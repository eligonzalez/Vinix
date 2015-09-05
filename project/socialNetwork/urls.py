from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^home_social', views.home_social, name='home_social'),
)