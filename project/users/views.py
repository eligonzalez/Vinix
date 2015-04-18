#Django Imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

#Util Imports

#Project Imports
from .forms import *
from .models import BasicUser


def login_view(request):
    if request.user.is_authenticated():
        pass
        #return redirect('login')
    form = BasicUserLoginForm()
    form_reg = BasicUserRegisterForm()
    errors = []
    return render(
        request,
        'login_register_view.html',
        {
            'form_reg': form_reg,
            'form': form,

            'form_register_check': 'register_check',
            'form_login_check': 'login_check',

            'errors': errors,
        }
    )


def login_check(request):
    if request.user.is_authenticated():
        pass
        #return redirect('login')
    errors = []
    form_reg = BasicUserRegisterForm()
    form = BasicUserLoginForm(request.POST or None)
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
                    pass
                    #return redirect('home')
                else:
                    errors.append("Account has been disabled!")
            else:
                #the authentication system was unable
                #to verify the username and password
                errors.append("The username and password were incorrect.")
                form = BasicUserLoginForm(
                    initial={'username': form.cleaned_data['username']})
    else:
        form = BasicUserLoginForm()
    return render(
        request,
        'login_register_view.html',
        {
            'form_reg': form_reg,
            'form': form,

            'form_register_check': 'register_check',
            'form_login_check': 'login_check',

            'errors': errors,
        })


def register_check(request):
    if request.user.is_authenticated():
        pass
        #return redirect('login')

    errors = []
    form_reg = BasicUserRegisterForm(request.POST or None)
    form = BasicUserLoginForm()

    if request.method == "POST":

        if form_reg.is_valid():
            cd = form_reg.cleaned_data

            client = BasicUser()
            client.username = cd["email"]
            client.first_name = cd["first_name"]
            client.last_name = cd["last_name"]
            client.email = cd["email"]
            client.password = cd["password"]
            client.save()

            return render(
                request,
                'hola.html',
                {}
            )

    return render(
        request,
        'login_register_view.html',
        {
            'form_reg': form_reg,
            'form': form,

            'form_register_check': 'register_check',
            'form_login_check': 'login_check',

            'errors': errors,
        })