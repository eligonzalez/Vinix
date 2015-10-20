from django.conf.urls import patterns, url
from . import views



urlpatterns = patterns(
    '',
    url(r'^home$', views.home, name='home'),
    url(r'^product/wine/(?P<wine_id>\d+)/$', views.wine_view, name='wine_view'),
    url(r'^list_wine/(?P<filter>[a-zA-Z]+)/(?P<value>[\w|\W]+)', views.list_wines_view, name='list_wine'),
    url(r'^add_wine_shopping$', views.add_wine_shopping, name='add_wine_shopping'),
    url(r'^search$', views.search, name='search'),
    url(r'^list_spirit/(?P<value>[a-zA-Z]+)/$', views.list_spirit, name='list_spirit'),
    url(r'^product/spirit/(?P<spirit_id>\d+)/$', views.spirit_view, name='spirit_view'),
    url(r'^add_comment_product$', views.add_comment_product, name='add_comment_product'),
    url(r'^remove_comment_product/(?P<product_id>\d+)/(?P<user_id>\d+)/$', views.remove_comment_product, name='remove_comment_product'),
    url(r'^products_favorite$', views.products_favorite, name='products_favorite'),
)