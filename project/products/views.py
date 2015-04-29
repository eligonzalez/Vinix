
from django.shortcuts import render
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *

admin.autodiscover()

def home_view(request):
    prodZone = Zone.objects.all()
    prodStyle = Style.objects.all()
    prodVarietal = Varietal.objects.all()
    destYLicor = SubTypeSpirit.objects.all()

    wines = Wine.objects.all().order_by('name')
    paginator = Paginator(wines, 12)
    page = request.GET.get('page')

    try:
        prod_page = paginator.page(page)
    except PageNotAnInteger:
        prod_page = paginator.page(1)
    except EmptyPage:
         prod_page = paginator.page(paginator.num_pages)

    return render(request,'home_view.html',
        {
            'products': wines,
            'list_prod': prod_page
        }
    )

def wine_view(request, wine_id):
    wine_data = get_object_or_404(Wine, pk=wine_id)
    return render(request,'wine_view.html',
        {
            'wine_data': wine_data,
        }
    )

def list_wines_view(request, filter, value):

    prod = Wine.get_product_filter(filter, value)
    paginator = Paginator(prod, 4)
    page = request.GET.get('page')

    try:
        prodPage = paginator.page(page)
    except PageNotAnInteger:
        prodPage = paginator.page(1)
    except EmptyPage:
        prodPage = paginator.page(paginator.num_pages)

    return render(request,'list_wines.html',
        {
            'listProd' : prodPage, 'type' : prod[0].get_type_display()
        }
    )