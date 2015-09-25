from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^shopping_cart', views.shopping_cart, name='shopping_cart'),
    url(r'^finish_purchase', views.finish_purchase, name='finish_purchase'),
    url(r'^check_finish_purchase', views.check_finish_purchase, name='check_finish_purchase'),
    url(r'^summary_shopping/(?P<idShopping>\d+)/', views.summary_shopping, name='summary_shopping'),

)