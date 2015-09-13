from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from users.models import *
from socialNetwork.models import *
from products.models import *
from products.forms import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.db.models import Q

def profile(request, idUser):

    profile = Follower.get_profile(idUser)
    return render(request, 'profile.html', profile)

def followers(request):

    friends = Follower.get_friends(request.user)
    return render(request, 'follower.html', friends)

def remove_followers(request, follower, followed):

    Follower.delete_followers(follower, followed)
    friends = Follower.get_friends(request.user)
    return render(request, 'follower.html', friends)

def add_followers(request,follower, followed):

    Follower.add_followers(follower, followed)
    friends = Follower.get_friends(request.user)
    return render(request, 'follower.html', friends)

def search_people(request):

    sigues = Follower.objects.filter(idUser1=request.user.id)
    friends = []

    for s in sigues:
        friends.append(BasicUser.objects.get(id=str(s.idUser2)))

    if request.method == 'POST':
        form = searchForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            people = BasicUser.objects.filter(Q(first_name__icontains=word) | Q(last_name__icontains=word) | Q(username__icontains=word)).exclude(id=request.user.id)
            unknowables = filter(lambda x: x not in set(friends), people)
            return render(request,'follower.html', {'word': word, 'people': unknowables, 'friends': friends})

    return render(request, 'follower.html', {})

def add_post(request):

    if request.method == 'POST':
        form = addPostForm(request.POST)

        if form.is_valid():
            post = form.cleaned_data['post']
            idReceiver = form.cleaned_data['receiver']

            info = Follower.add_post_function(post, idReceiver, request.user)
            return render(request, 'profile.html', info)

    return render(request, 'profile.html', {})

def remove_post(request, idPost, idUser):

    info = Post.delete_post(idPost, idUser)
    return render(request, 'profile.html', info)

def home_social(request):

    posts = Post.objects.filter(Q(idUser1=request.user) | Q(idUser2=request.user)).order_by('-date')
    user = BasicUser.objects.get(id=request.user.id)

    return render(request, 'home_social.html', {'user': user, 'posts': posts})

def wines_social(request):

    info = FavoriteProduct.get_products_favorite(request.user)
    return render(request, 'wine_social.html', info)

def search_wine(request):

    prod_favorite = FavoriteProduct.objects.filter(user=request.user)
    productsFavorite = []

    for p in prod_favorite:
        productsFavorite.append(Product.objects.get(id=str(p.product.id)))

    if request.method == 'POST':
        form = searchForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            winesAll = Product.objects.filter(Q(name__icontains=word))
            productsNoFavorite = filter(lambda x: x not in set(productsFavorite), winesAll)

            return render(request,'wine_social.html', {'word': word, 'productsNoFavorite': productsNoFavorite, 'productsFavorite': productsFavorite})

    return render(request, 'follower.html', {})

def add_favorite_product(request, idProduct):

    FavoriteProduct.add_product_favorite(idProduct, request.user)
    favoriteProducts = FavoriteProduct.get_products_favorite(request.user)
    return render(request, 'wine_social.html', favoriteProducts)

def remove_favorite_product(request, idProduct):

    FavoriteProduct.delete_product_favorite(idProduct, request.user)
    favoriteProducts = FavoriteProduct.get_products_favorite(request.user)

    return render(request, 'wine_social.html', favoriteProducts)