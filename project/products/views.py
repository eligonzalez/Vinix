#Django Imports
from django.shortcuts import render
from django.contrib import admin
from django.shortcuts import get_object_or_404
#Util Imports


#Project Imports
from .models import Wine, Product
# Create your views here.

admin.autodiscover()

def home_view(request):
    wines = Wine.objects.all().order_by('?')[:12]
    for i in wines:
        print(i)
    return render(
        request,
        'home_view.html',
        {
            'products': wines,
        }
    )

def wine_view(request, wine_id):
    wine_data = get_object_or_404(Wine, pk=wine_id)
    return render(
        request,
        'wine_view.html',
        {
            'wine_data': wine_data,
        }
    )