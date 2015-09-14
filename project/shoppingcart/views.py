from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from shoppingcart.models import *
from users.models import *
from .forms import *


def shopping_cart(request):
    if not request.user.is_authenticated():
        return redirect('login')

    request.session['amount'] = float(Shopping.get_amount(request.user))
    shopping = Shopping.get_products(user=request.user.id)
    total = Shopping.get_amount(user=request.user.id)
    priceXAmount = Shopping.get_pricexAmount_product(shopping)
    errors=[]

    if request.method == 'POST':
        if not "checkbox" in request.POST.keys():
            errors.append("Debe aceptar los términos y condiciones para poder continuar.")
        else :
             return redirect('finish_purchase')


    return render(request, "shopping_cart.html",
                  {'shopping_cart': shopping,'total' : total,'priceProduct' : priceXAmount,'errors' : errors,
                   'prodZone':Zone.objects.all(),'prodStyle':Style.objects.all(),'prodVarietal':Varietal.objects.all(),
                   'destYLicor': SubTypeSpirit.objects.all()
                })


''' Falta poder editar la direccion de usuario '''
def finish_purchase(request):
    if not request.user.is_authenticated():
        return redirect('login')

    address = AddressUser.objects.get(idUser=request.user.id)
    shopping = Shopping.get_products(request.user)
    totalPrice = Shopping.get_amount(request.user)

    general = Product.get_general()
    specific = {'user' : request.user,'address' : address,'shopping' : shopping,'total' : totalPrice}
    total = dict(general.items() | specific.items())
    return render(request, "finish_purchase.html",total)


def check_finish_purchase(request):

    if not request.user.is_authenticated():
        return redirect('login')

    if request.method == 'POST':
        form = finishPurchase_Form(request.POST)
        client = BasicUser.objects.get(id=request.user.id)

        message = None
        error = None

        if form.is_valid():
            error = "alert alert-success"
            message = "La compra se ha realizado correctamente."
            Shopping.accept_purchase(client)

        else :
            error = "alert alert-danger"
            message = "Introduzca el nombre de la tarjeta correctamente."

        address = AddressUser.objects.get(idUser=request.user.id)
        shopping = Shopping.get_products(request.user)
        totalPrice = Shopping.get_amount(request.user)

        general = Product.get_general()
        specific = {'user' : request.user,'address' : address,'shopping' : shopping,'total' : totalPrice,'message' : message,'error': error}
        total = dict(general.items() | specific.items())
        return render(request, "finish_purchase.html",total)
    else :
        return redirect('finish_purchase')