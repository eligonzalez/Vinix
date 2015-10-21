from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from users.models import *
from socialNetwork.models import *
from products.models import *
from products.forms import *
from .forms import *
from django.template import RequestContext
from django.db.models import Q
from django.core.urlresolvers import reverse

def profile(request, idUser):

    profile = Follower.get_profile(idUser)
    user = BasicUser.objects.get(id=str(idUser))
    productsFav = FavoriteProduct.get_products_favorite(user)
    specific = {'form': UploadFileForm()}
    total = dict(profile.items() | specific.items())
    total['productsFav'] = productsFav['productsFavorite']
    return render(request, 'profile.html', total)

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

    return redirect('error')

def add_post(request):

    if request.method == 'POST':
        form = addPostForm(request.POST)

        if form.is_valid():
            post = form.cleaned_data['post']
            idReceiver = form.cleaned_data['receiver']
            info = Follower.add_post_function(post, idReceiver, request.user)
            return redirect('profile', idReceiver)

    return redirect('error')

def remove_post(request, idPost, idUser):

    info = Post.delete_post(idPost, idUser)
    return redirect('profile', idUser)

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

    info = FavoriteProduct.get_products_favorite(request.user)

    if request.method == 'POST':
        form = searchForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            winesAll = Product.objects.filter(Q(name__icontains=word))
            productsNoFavorite = filter(lambda x: x not in set(productsFavorite), winesAll)

            return render(request,'wine_social.html', {'word': word, 'productsNoFavorite': productsNoFavorite, 'productsFavorite': info['productsFavorite']})

    return redirect('error')

def add_favorite_product(request, idProduct):
    if not request.user.is_authenticated():
        return redirect('login')

    FavoriteProduct.add_product_favorite(idProduct, request.user)
    return redirect('wines_social')

def remove_favorite_product(request, idProduct):

    FavoriteProduct.delete_product_favorite(idProduct, request.user)
    return redirect('wines_social')

def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            user = BasicUser.objects.get(id=request.user.id)
            user.image = request.FILES['image']
            user.save()
            return HttpResponseRedirect(reverse('imageupload'))
    else:
        form = UploadFileForm()
    return redirect('profile', request.user.id)
