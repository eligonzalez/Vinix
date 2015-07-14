from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from shoppingcart.models import *


def login_view(request):
    if request.user.is_authenticated():
        return redirect('my_account')
    form = BasicUserLoginForm()
    form_reg = BasicUserRegisterForm()
    errors = []
    return render(request,'login_register_view.html',
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
        return redirect('my_account')
    errors = []
    form_reg = BasicUserRegisterForm()
    form = BasicUserLoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            #form login
            print(form.cleaned_data['username'])
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                # the password verified for the user
                if user.is_active:
                    login(request, user)
                    request.session['amount'] = float(Shopping.get_amount(request.user))

                    return redirect('home')
                else:
                    errors.append("La cuenta ha sido deshabilitada.")
            else:
                #the authentication system was unable
                #to verify the username and password
                errors.append("Usuario y contraseña incorrectos")
                form = BasicUserLoginForm(
                    initial={'username': form.cleaned_data['username']})
    else:
        form = BasicUserLoginForm()
    return render(request,'login_register_view.html',
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
        return redirect('home')

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
            client.set_password(cd["password"])
            client.save()

            user = authenticate(
                username=client.username,
                password=client.password,
            )
            #login(request, user)
            return redirect('home')

    return render(request,'login_register_view.html',
        {
            'form_reg': form_reg,
            'form': form,

            'form_register_check': 'register_check',
            'form_login_check': 'login_check',

            'errors': errors,
        })


def logout_view(request):
    logout(request)

    form = BasicUserLoginForm()
    form_reg = BasicUserRegisterForm()
    errors = []
    return render(request,'login_register_view.html',
        {
            'form_reg': form_reg,
            'form': form,

            'form_register_check': 'register_check',
            'form_login_check': 'login_check',

            'errors': errors,
        }
    )


def my_account(request):
    if not request.user.is_authenticated():
        return redirect('login')

    address = AddressUser.objects.get(idUser=2)
    shoppings = Shopping.objects.filter(user=2, finish=True)

    return render(request, "my_account.html",
      {
          'address' : address,
          'shoppings' : shoppings,
          'user' : request.user,
      })

def edit_account(request):

    if not request.user.is_authenticated():
        return redirect('login')

    if request.method == "GET":
        address = AddressUser.objects.get(idUser=2)

        return render(request, "edit_account.html",
          {
              'address' : address,
              'user' : request.user,
          })

    elif request.method == "POST":

        cd = edit_account_form(request.POST)
        if cd.is_valid():

            client = BasicUser(id=request.user.id)
            client.username = cd["email"]
            client.first_name = cd["first_name"]
            client.last_name = cd["last_name"]
            client.email = cd["email"]
            client.set_password(cd["password"])
            client.save()
            ad = AddressUser.objects.get(idUser=2)
            ad.address = cd["address"]
            ad.province = cd["province"]
            ad.country = cd["country"]
            ad.postalCode = cd["postalCode"]
            ad.phone = cd["phone"]
            ad.save()
            return redirect('my_account')
        else :
            return redirect('home')