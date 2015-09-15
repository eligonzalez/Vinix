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

    products = ProductFilter(request.GET, queryset=Product.objects.all())
    general = Product.get_general()
    pagination = Product.get_pagination(request,products,12)
    specific = {'products': products,'filter': products}
    total = dict(general.items() | specific.items() | pagination.items())
    return render(request,'home_view.html', total )

def wine_view(request, wine_id):

    wine_data = get_object_or_404(Wine, pk=wine_id)
    general = Product.get_general()
    specific = {'wine_data': wine_data}
    total = dict(general.items() | specific.items())
    return render(request,'wine_view.html',total)

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
            request.session['amount'] = float(Shopping.get_amount(request.user))

            if result == 1 :
                error = "alert alert-danger"
                message = "El producto ya existe"
            else :
                error = "alert alert-success"
                message = "Se ha añadido correctamente"

            general = Product.get_general()

            product_data = get_object_or_404(Product, pk=idProd)
            if hasattr(product_data, 'spirit'):
                spirit_data = get_object_or_404(Spirit, pk=idProd)
                specific = {'spirit_data': spirit_data, 'message' : message, 'error': error}
                total = dict(general.items() | specific.items())
                return render(request,'spirit.html', total)

            else:
                wine_data = get_object_or_404(Wine, pk=idProd)
                specific = {'wine_data': wine_data, 'message' : message, 'error': error}
                total = dict(general.items() | specific.items())
                return render(request,'wine_view.html', total)
    else :
        return render(request,'wine_view.html', {})

def list_wines_view(request, filter, value):

    filters = Wine.get_product_filter(filter,value)

    general = Product.get_general()
    pagination = Product.get_pagination(request,filters['prod'], 4)
    total = dict(filters.items() | pagination.items() | general.items())

    return render(request,'list_wines.html', total)

def search(request):

    if request.method == 'POST':
        form = searchForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            prod = Wine.objects.filter(Q(name__icontains=word))

            specific = {'word':word}
            general = Product.get_general()
            pagination = Product.get_pagination(request,prod,4)
            total = dict(specific.items() | pagination.items() | general.items())
            return render(request,'search.html',total)

    return render(request,'home_view.html')

def list_spirit(request, value):

    filters = Spirit.get_products_filter(value)

    general = Product.get_general()
    pagination = Product.get_pagination(request,filters['prod'], 4)
    total = dict(filters.items() | pagination.items() | general.items())
    return render(request,'list_spirit.html', total)

def spirit_view(request, spirit_id):

    spirit_data = get_object_or_404(Spirit, pk=spirit_id)
    general = Product.get_general()
    specific = {'spirit_data': spirit_data}
    total = dict(general.items() | specific.items())
    return render(request,'spirit.html',total)