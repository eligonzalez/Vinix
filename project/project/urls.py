from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('products.urls')),
    url(r'^', include('shoppingcart.urls')),
    url(r'^', include('users.urls')),
    url(r'^', include('socialNetwork.urls')),
    url(r'^admin/', include(admin.site.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
