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
    seguidos = Follower.objects.filter(idUser1=idUser)
    teSiguen = Follower.objects.filter(idUser2=idUser)
    posts = Post.objects.filter(idUser2=idUser).order_by('-date')
    user = BasicUser.objects.get(id=str(idUser))

    return render(request, 'profile.html', {
        'user': user,
        'seguidos': seguidos,
        'numSeguidos': (len(seguidos)),
        'teSiguen': teSiguen,
        'numTeSiguen': (len(teSiguen)),
        'posts': posts,
        'numPosts': (len(posts)),
        'request': request
    })

def followers(request):
    sigues = Follower.objects.filter(idUser1=request.user)
    friends = []

    for s in sigues:
        friends.append(BasicUser.objects.get(id=str(s.idUser2)))
    return render(request, 'follower.html', {'user': request.user, 'friends': friends})

def remove_followers(request, follower, followed):
    r = Follower.objects.filter(idUser1=follower, idUser2=followed)
    r.delete()

    sigues = Follower.objects.filter(idUser1=request.user)
    friends = []
    for s in sigues:
        friends.append(BasicUser.objects.get(id=str(s.idUser2)))
    return render(request, 'follower.html', {'user': request.user, 'friends': friends})

def add_followers(request,follower, followed):
    f1 = BasicUser.objects.get(id=str(follower))
    f2 = BasicUser.objects.get(id=str(followed))
    if f1 != f2 and not Follower.objects.filter(idUser1=f1, idUser2=f2).exists():
        ad = Follower(idUser1=f1, idUser2=f2)
        ad.save()
    #else:
        #Mensaje de error

    sigues = Follower.objects.filter(idUser1=request.user)
    friends = []
    for s in sigues:
        friends.append(BasicUser.objects.get(id=str(s.idUser2)))
    return render(request, 'follower.html', {'user': request.user, 'friends': friends})

def search_people(request):

    sigues = Follower.objects.filter(idUser1=request.user)
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
            receiver = BasicUser.objects.get(id=str(idReceiver))
            user = BasicUser.objects.get(id=request.user.id)


            if Follower.objects.filter(idUser1=request.user, idUser2=receiver).exists() or idReceiver == request.user.id:
                ad = Post(idUser1=user, idUser2=receiver, comment=post)
                ad.save()
            else:
                print("Tienes que seguir a este usuario para poder escribirle un comentario.")
                
            seguidos = Follower.objects.filter(idUser1=receiver.id)
            teSiguen = Follower.objects.filter(idUser2=receiver.id)
            posts = Post.objects.filter(idUser2=receiver.id).order_by('-date')

            return render(request,'profile.html', {'user': receiver,'seguidos': seguidos,'posts':posts,
                'numSeguidos': (len(seguidos)), 'teSiguen': teSiguen, 'numTeSiguen': (len(teSiguen)),'numPosts': (len(posts))
            })

    return render(request, 'profile.html', {
        'user': receiver,
        'seguidos': seguidos,
        'numSeguidos': (len(seguidos)),
        'teSiguen': teSiguen,
        'numTeSiguen': (len(teSiguen)),
        'posts': posts,
        'numPosts': (len(posts))
    })

def remove_post(request, idPost, idUser):

    post = Post.objects.get(id=idPost)
    receiver = BasicUser.objects.get(id=str(post.idUser2))
    seguidos = Follower.objects.filter(idUser1=receiver.id)
    teSiguen = Follower.objects.filter(idUser2=receiver.id)
    user = BasicUser.objects.get(id=str(idUser))

    if str(post.idUser1) == str(idUser) or str(post.idUser2) == str(idUser):
        post.delete()
    else:
        print("Estás eliminando un mensaje que no ha sido escrito por ti.")

    posts = Post.objects.filter(idUser2=receiver.id).order_by('-date')
    return render(request, 'profile.html', {'user': user,
        'seguidos': seguidos,
        'numSeguidos': (len(seguidos)),
        'teSiguen': teSiguen,
        'numTeSiguen': (len(teSiguen)),
        'posts': posts,
        'numPosts': (len(posts)),
        'user': receiver})

def home_social(request):

    posts = Post.objects.filter(Q(idUser1=request.user) | Q(idUser2=request.user)).order_by('-date')
    user = BasicUser.objects.get(id=request.user.id)

    return render(request, 'home_social.html', {'user': user, 'posts': posts})

def wines_social(request):
    prod_favorite = FavoriteProduct.objects.filter(user=request.user)
    productsFavorite = []

    for p in prod_favorite:
        productsFavorite.append(Product.objects.get(id=str(p.product.id)))

    return render(request, 'wine_social.html', {'user': request.user, 'productsFavorite': productsFavorite})

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
    p = Product.objects.get(id=str(idProduct))
    user = BasicUser.objects.get(id=request.user.id)

    if not FavoriteProduct.objects.filter(user=request.user, product=p).exists():
        ad = FavoriteProduct(user=user, product=p)
        ad.save()
    #else:
        #Mensaje de error

    prod_favorite = FavoriteProduct.objects.filter(user=request.user)
    productsFavorite = []

    for p in prod_favorite:
        productsFavorite.append(Product.objects.get(id=str(p.product.id)))

    return render(request, 'wine_social.html', {'user': request.user, 'productsFavorite': productsFavorite})

def remove_favorite_product(request, idProduct):

    r = FavoriteProduct.objects.filter(user=request.user, product= idProduct)
    r.delete()

    prod_favorite = FavoriteProduct.objects.filter(user=request.user)
    productsFavorite = []

    for p in prod_favorite:
        productsFavorite.append(Product.objects.get(id=str(p.product.id)))

    return render(request, 'wine_social.html', {'user': request.user, 'productsFavorite': productsFavorite})
