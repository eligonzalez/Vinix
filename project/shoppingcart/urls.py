from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^shopping_cart', views.shopping_cart, name='shopping_cart'),

)