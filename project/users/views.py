from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *
from shoppingcart.models import *
from django.db.models import Q


def login_view(request):
    form = BasicUserLoginForm()
    form_reg = BasicUserRegisterForm()
    errors = []

    general = Product.get_general()
    specific = {'form_reg': form_reg, 'form': form, 'form_register_check': 'register_check', 'form_login_check': 'login_check', }
    total = dict(general.items() | specific.items())
    total['errors'] = errors
    return render(request, 'login_register_view.html', total)

def login_check(request):
    if request.user.is_authenticated():
        return redirect('my_account')
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
                    request.session['amount'] = float(Shopping.get_amount(request.user))

                    return redirect('home')
                else:
                    errors.append("La cuenta ha sido deshabilitada.")
            else:
                #the authentication system was unable
                #to verify the username and password
                errors.append("Usuario y contraseña incorrectos")
                form = BasicUserLoginForm(initial={'username': form.cleaned_data['username']})
    else:
        form = BasicUserLoginForm()

    general = Product.get_general()
    specific = {'form_reg': form_reg, 'form': form, 'form_register_check': 'register_check', 'form_login_check': 'login_check',}
    total = dict(general.items() | specific.items())
    total['errors'] = errors
    return render(request,'login_register_view.html', total)


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
            client.image = 'images/iconoPersona.jpg'
            client.save()



            #login(request, user)
            firstShopping = Shopping(user=client)
            firstShopping.save()
            firstAddress = AddressUser(idUser=client)
            firstAddress.save()


            user = authenticate(
                username=client.username,
                password=cd["password"],
            )

            if user is not None:
                login(request, user)
                print (request)

            return redirect('home')

    return render(request,'login_register_view.html', {'form_reg': form_reg, 'form': form, 'form_register_check': 'register_check',
            'form_login_check': 'login_check', 'errors': errors})


def logout_view(request):
    logout(request)

    form = BasicUserLoginForm()
    form_reg = BasicUserRegisterForm()
    errors = []
    return render(request,'login_register_view.html', {'form_reg': form_reg, 'form': form, 'form_register_check': 'register_check',
            'form_login_check': 'login_check', 'errors': errors})


def my_account(request):
    if not request.user.is_authenticated():
        return redirect('login')

    address = AddressUser.objects.filter(idUser=request.user.id)
    shoppings = Shopping.objects.filter(user=request.user.id, finish=True)

    general = Product.get_general()
    specific = {'address': address, 'shoppings': shoppings, 'user': request.user}
    total = dict(general.items() | specific.items())
    return render(request, "my_account.html", total)

def edit_account(request):

    if not request.user.is_authenticated():
        return redirect('login')

    if request.method == "GET":
        address = AddressUser.objects.filter(idUser=request.user.id)

        return render(request, "edit_account.html",
          {
              'address' : address,
              'user' : request.user,
          })

    elif request.method == "POST":

        cd = edit_account_form(request.POST)

        if cd.is_valid():
            client = BasicUser.objects.get(id=request.user.id)
            AddressUser.set_AddressUser(request.user,cd)
            resultUser = BasicUser.set_BasicUser(client,cd)

            if resultUser == 1:
                error = "alert alert-danger"
                message = "Las contraseñas han de coincidir"
            else :
                error = "alert alert-success"
                message = "Los datos han sido modificados"

            address = AddressUser.objects.filter(idUser=request.user.id)
            return render(request, "edit_account.html", {'address' : address, 'user' : request.user, 'error' : error, 'message' : message})
        else:
            return redirect('home')

def error(request):
    general = Product.get_general()
    return render(request, 'error.html', general)