from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^login$', views.login_view, name='login'),
    url(r'^logout', views.logout_view, name='logout'),
    url(r'^login_check$', views.login_check, name='login_check'),
    url(r'^register_check$', views.register_check, name='register_check'),
    url(r'^my_account', views.my_account, name='my_account'),
)