
from django.shortcuts import render
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
from shoppingcart.models import *

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

def add_wine_shopping(request):
    message = []

    if request.method == 'POST':
        form = addProduct(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            idProd = form.cleaned_data['idProd']
            result= Shopping_Cart.add_Product_Shopping_Cart(2,idProd, amount)
            product = Product.objects.get(id=idProd)

            if result == 1 :
                message.append("El producto ya existe")
            else :
                message.append("Se ha añadido correctamente")
            return render(request,'wine_view.html', {'wine_data': product, 'message' : message})

    else :
        return render(request,'wine_view.html', {'wine_data': wine_data})

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