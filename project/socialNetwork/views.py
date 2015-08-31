from django.shortcuts import render, render_to_response
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import BaseUserLoginForm, BaseUserRegisterForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def home(request):
    users = BasicUser.objects.all()
    return render(request, 'home.html', {'people': users})


def login_view(request):
    if request.user.is_authenticated():
        return redirect('home')
    form = BaseUserLoginForm()
    form_reg = BaseUserRegisterForm()
    return render(request, 'login.html', {
            'form': form,
            'form_reg': form_reg,
            'form_action': 'loginf',
            'form_action_reg': 'register',
        }
    )


def login_form(request):
    if request.user.is_authenticated():
        return redirect('home')
    errors = []
    form_reg = BaseUserRegisterForm()
    form = BaseUserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            #form login
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    errors.append("Account has been disabled!")
            else:
                #the authentication system was unable
                #to verify the username and password
                errors.append("The username and password were incorrect.")
                form = BaseUserLoginForm(
                    initial={'username': form.cleaned_data['username']})
    else:
        form = BaseUserLoginForm()
    return render(request,'login.html',
        {
            'form_reg': form_reg,
            'form': form,
            'form_action': 'loginf',
            'form_action_reg': 'register',
            'errors': errors,
        }
    )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('home')


def register(request):
    if request.user.is_authenticated():
        return redirect('home')
    form = BaseUserLoginForm()
    form_reg = BaseUserRegisterForm(request.POST or None)
    if request.method == "POST":
        if form_reg.is_valid():
            cd = form_reg.cleaned_data
            person = BasicUser()
            person.username = cd['username']
            person.email = cd['email']
            person.set_password(cd['password'])
            person.birth_date = cd['birth_date']
            person.first_name = cd['first_name']
            person.last_name = cd['last_name']
            person.save()
            return render(request, 'reg_succeed.html',
                {
                    'username': cd['username'],
                    'email': cd['email']
                }
            )
    return render(request, 'login.html',
        {
            'form_reg': form_reg,
            'form': form,
            'form_action': 'loginf',
            'form_action_reg': 'register',
        }
    )


def profiler(request, username):
    k = get_object_or_404(BasicUser, username=username)
    following = k.relationships.following()
    return render_to_response("profile.html",
        {
            'people': following,
            'username': username
        },
        context_instance=RequestContext(request)
    )


def add_follower(request, follow):
    us = get_object_or_404(BasicUser, username=follow)
    request.user.relationships.add(us)
    following = us.relationships.following()
    return render_to_response("profile.html",
        {
            'following': following,
            'follow': follow,
            'username': follow.title()
        },
        context_instance=RequestContext(request)
    )


def remove_follower(request, follow):
    us = get_object_or_404(BasicUser, username=follow)
    request.user.relationships.remove(us)
    following = us.relationships.following()
    return render_to_response("profile.html",
        {
            'following': following,
            'follow': follow,
            'username': follow.title()
        },
        context_instance=RequestContext(request)
    )
