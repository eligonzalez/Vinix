from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from users.models import *
from socialNetwork.models import *
from products.forms import *
from django.shortcuts import get_object_or_404
from django.template import RequestContext
from django.db.models import Q



def profile(request):
    seguidos = Follower.objects.filter(idUser1=request.user)
    teSiguen = Follower.objects.filter(idUser2=request.user)
    posts = Post.objects.filter(idUser=request.user)
    return render(request, 'profile.html', {
        'user': request.user,
        'seguidos': seguidos,
        'numSeguidos': (len(seguidos)),
        'teSiguen': teSiguen,
        'numTeSiguen': (len(teSiguen)),
        'posts': posts,
        'numPosts': (len(posts))
    })

def followers(request):
    sigues = Follower.objects.filter(idUser1=request.user)
    friends = []
    for s in sigues:
        print(s.idUser2)
        friends.append(BasicUser.objects.get(id=str(s.idUser2)))
    return render(request, 'follower.html', {'user': request.user, 'friends': friends})

def remove_followers(request, follower, followed):
    r = Follower.objects.filter(idUser1=follower, idUser2=followed)
    r.delete()

    sigues = Follower.objects.filter(idUser1=request.user)
    friends = []
    for s in sigues:
        print(s.idUser2)
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
        print(s.idUser2)
        friends.append(BasicUser.objects.get(id=str(s.idUser2)))
    return render(request, 'follower.html', {'user': request.user, 'friends': friends})

def search_people(request):

    sigues = Follower.objects.filter(idUser1=request.user)
    friends = []
    for s in sigues:
        print(s.idUser2)
        friends.append(BasicUser.objects.get(id=str(s.idUser2)))

    if request.method == 'POST':
        form = searchForm(request.POST)

        if form.is_valid():
            word = form.cleaned_data['word']
            people = BasicUser.objects.filter(Q(first_name__icontains=word))
            print(people)
            return render(request,'follower.html', {'word': word, 'people': people, 'friends': friends})

    return render(request, 'follower.html', {'people': people, 'friends': friends, 'word': word})