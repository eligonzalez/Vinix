from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
from shoppingcart.models import *
from .filters import *
from django.db.models import Q

admin.autodiscover()

def home(request):
    products = ProductFilter(request.GET, queryset=Product.objects.all())

    has_filters = False
    if ('o' in request.GET):
        has_filters = True
        filter_value = '&o='+request.GET['o']
        print (request.GET['o'])


    general = Product.get_general()
    pagination = Product.get_pagination(request, products, 4)

    specific = {'products': products, 'has_filters': has_filters}
    if specific['has_filters']== True:
        specific['filter_value'] = filter_value

    total = dict(general.items() | specific.items() | pagination.items())
    return render(request, 'home.html', total)

def wine_view(request, wine_id):

    wine_data = get_object_or_404(Wine, pk=wine_id)

    comments = PunctuationProduct.objects.filter(product=wine_data).order_by('-date')
    comment_user = PunctuationProduct.objects.filter(user=request.user, product=wine_data).exists()
    favorite = FavoriteProduct.objects.filter(user=request.user, product=wine_data)

    general = Product.get_general()
    specific = {'wine_data': wine_data, 'comments': comments, 'comment_user': comment_user, 'favorite': favorite}
    total = dict(general.items() | specific.items())
    return render(request,'wine.html', total)

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
                return render(request,'wine.html', total)

    return redirect('error')

def list_wines_view(request, filter, value):

    typeProd = None

    if filter == 'type':
        prod = ProductFilter(request.GET, queryset=Wine.objects.filter(type=value))

        if value == 'B':
            typeProd = 'Vinos blancos'
        elif value == 'T':
            typeProd = 'Vinos tintos'
        elif value == 'R':
            typeProd = 'Vinos rosados'
        elif value == 'E':
            typeProd = 'Vinos espumosos'

    elif filter == 'zone':
        prod = ProductFilter(request.GET, queryset=Product.objects.filter(zone__name=value))
        typeProd = 'Zona ' + value
    elif filter == 'style' :
        prod = ProductFilter(request.GET, queryset=Wine.objects.filter(style__name=value))
        typeProd = 'Estilo ' + value
    elif filter == 'varietal' :
        prod = ProductFilter(request.GET, queryset=Wine.objects.filter(varietal__name=value))
        typeProd = 'Variedad ' + value
    elif filter == 'priceLower' :
        prod = ProductFilter(request.GET, queryset=Product.objects.filter(price__range=(0,9.99)))
        typeProd = 'Vinos por menos de 10€'
    elif filter == 'priceUpper' :
        prod = ProductFilter(request.GET, queryset=Product.objects.filter(price__range=(10,20)))
        typeProd = 'Vinos entre 10€ y 20€'


    has_filters = False
    if ('o' in request.GET):
        has_filters = True
        filter_value = '&o='+request.GET['o']
        print (request.GET['o'])

    general = Product.get_general()
    specific = {'type': typeProd, 'products': prod, 'has_filters': has_filters}

    if specific['has_filters']== True:
        specific['filter_value'] = filter_value

    pagination = Product.get_pagination(request,prod,12)
    total = dict(specific.items() | general.items() | pagination.items())
    return render(request,'list_wines.html', total)

def search(request):

    if request.method == 'POST':
        form = searchForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            prod = Product.objects.filter(Q(name__icontains=word))

            specific = {'word': word}
            general = Product.get_general()
            pagination = Product.get_pagination(request,prod,4)
            total = dict(specific.items() | pagination.items() | general.items())
            return render(request,'search.html',total)

    return redirect('error')

def list_spirit(request, value):

    typeProd = value
    products = ProductFilter(request.GET, queryset=Spirit.objects.filter(subType__name=value))

    has_filters = False
    if ('o' in request.GET):
        has_filters = True
        filter_value = '&o='+request.GET['o']
        print (request.GET['o'])

    general = Product.get_general()
    pagination = Product.get_pagination(request,products, 12)
    specific = {'type' : typeProd, 'products': products, 'has_filters': has_filters}

    if specific['has_filters']== True:
        specific['filter_value'] = filter_value

    total = dict(specific.items() | pagination.items() | general.items())
    return render(request,'list_spirit.html', total)

def spirit_view(request, spirit_id):

    spirit_data = get_object_or_404(Spirit, pk=spirit_id)
    comments = PunctuationProduct.objects.filter(product=spirit_data).order_by('-date')
    comment_user = PunctuationProduct.objects.filter(user=request.user, product=spirit_data).exists()
    favorite = FavoriteProduct.objects.filter(user=request.user, product=spirit_data)

    general = Product.get_general()
    specific = {'spirit_data': spirit_data, 'comments': comments, 'comment_user' : comment_user, 'favorite': favorite}
    total = dict(general.items() | specific.items())
    return render(request,'spirit.html', total)

def add_comment_product(request):

    if request.method == 'POST':
        form = addCommentProduct(request.POST)

        if form.is_valid():
            c = form.cleaned_data['comment']
            idProduct = form.cleaned_data['idProduct']
            punctuation = form.cleaned_data['punctuation']

            p = Product.objects.get(id=idProduct)
            PunctuationProduct.add_comment(p, c, punctuation, request.user)

            if hasattr(p, 'spirit'):
                return redirect('spirit_view', idProduct)
            else:
                return redirect('wine_view', idProduct)

    return redirect('error')

def remove_comment_product(request, product_id, user_id):
    p = Product.objects.get(id=product_id)

    PunctuationProduct.delete_comment(p, user_id, request.user)

    if hasattr(p, 'spirit'):
        return redirect('spirit_view', product_id)
    else:
        return redirect('wine_view', product_id)

def products_favorite(request):
    if not request.user.is_authenticated():
        return redirect('login')

    favorite = PunctuationProduct.favorite_punctuation_product(request.user)

    general = Product.get_general()
    total = dict(general.items() | favorite.items())
    return render(request, 'productsFavorite.html', total)


