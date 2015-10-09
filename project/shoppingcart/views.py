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
    total = float(Shopping.get_amount(user=request.user.id)) + 3.00
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
                   'destYLicor': SubTypeSpirit.objects.all()})


def finish_purchase(request):
    if not request.user.is_authenticated():
        return redirect('login')

    purcharse = Shopping_Cart.get_finish_purchase(request.user)
    general = Product.get_general()
    total = dict(general.items() | purcharse.items())
    return render(request, "finish_purchase.html", total)


def check_finish_purchase(request):

    if not request.user.is_authenticated():
        return redirect('login')

    if request.method == 'POST':
        form = finishPurchase_Form(request.POST)

        shop = Shopping_Cart.set_finish_purchase(request.user, form)

        general = Product.get_general()
        total = dict(general.items() | shop.items())
        return render(request, "finish_purchase.html", total)
    else:
        return redirect('finish_purchase')


def summary_shopping(request, idShopping):

    shopping = Shopping.objects.get(id=idShopping)
    shoppingCart = Shopping_Cart.objects.filter(shopping=shopping)

    general = Product.get_general()
    specific = {'shopping': shopping, 'shoppingCart': shoppingCart}
    total = dict(general.items() | specific.items())

    return render(request, 'summary_shopping.html',total)

def remove_product_shopping(request, idShopping, idProduct):

    print(idShopping)

    shopping = Shopping.objects.get(id=idShopping)
    product = Product.objects.get(id=idProduct)

    shoppingCart = Shopping_Cart.objects.filter(shopping=shopping, product=product)
    shoppingCart.delete()

    return redirect('shopping_cart')