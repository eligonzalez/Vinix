
from django.shortcuts import render
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
from shoppingcart.models import *
from .filters import *
from django.db.models import Q

admin.autodiscover()

def home_view(request):
    prodZone = Zone.objects.all()
    prodStyle = Style.objects.all()
    prodVarietal = Varietal.objects.all()
    destYLicor = SubTypeSpirit.objects.all()

    wines = ProductFilter(request.GET, queryset=Wine.objects.all())
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
            'list_prod': prod_page,
            'prodZone': prodZone,'prodStyle':prodStyle, 'prodVarietal':prodVarietal,
            'filter': wines
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
    message = None
    error = None
    wine_data = None

    if request.method == 'POST':
        form = addProduct(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            idProd = form.cleaned_data['idProd']
            result= Shopping_Cart.add_Product_Shopping_Cart(request.user,idProd, amount)
            wine_data = get_object_or_404(Wine, pk=idProd)

            if result == 1 :
                error = "alert alert-danger"
                message = "El producto ya existe"
            else :
                error = "alert alert-success"
                message = "Se ha añadido correctamente"
            return render(request,'wine_view.html', {'wine_data': wine_data, 'message' : message, 'error': error})

    else :
        return render(request,'wine_view.html', {'wine_data': wine_data})

def list_wines_view(request, filter, value):

    typeProd = None

    if filter == 'type' :
        prod = Wine.objects.filter(type=value)
        p = prod[0]
        typeProd = p.get_type_display()
    elif filter == 'zone' :
        prod = Product.objects.filter(zone__name=value)
        typeProd = 'por zona'
    elif filter == 'style' :
        prod = Wine.objects.filter(style__name=value)
        typeProd = 'por estilo'
    elif filter == 'varietal' :
        prod = Wine.objects.filter(varietal__name=value)
        typeProd = 'por variedad'
    elif filter == 'priceLower' :
        prod = Product.objects.filter(price__range=(0,9.99))
        typeProd = 'por menos de 10€'
    elif filter == 'priceUpper' :
        prod = Product.objects.filter(price__range=(10,20))
        typeProd = 'entre 10€ y 20€'

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
            'listProd' : prodPage, 'type' : typeProd
        }
    )

def search(request):

    if request.method == 'POST':
        form = searchForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            prod = Wine.objects.filter(Q(name__icontains=word))

            paginator = Paginator(prod, 4)
            page = request.GET.get('page')

            try:
                prodPage = paginator.page(page)
            except PageNotAnInteger:
                prodPage = paginator.page(1)
            except EmptyPage:
                prodPage = paginator.page(paginator.num_pages)

            return render(request,'search.html',
                {
                    'products' :  prodPage, 'word' : word
                }
            )

    return render(request,'home_view.html')