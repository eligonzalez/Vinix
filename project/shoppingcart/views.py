from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from shoppingcart.models import *
from users.models import *


''' Falta comprobar que los términos y condiciones este chekeado '''
def shopping_cart(request):
    if not request.user.is_authenticated():
        return redirect('login')

    shopping = Shopping.get_products(user=2)
    amount = Shopping.get_amount(user=2)
    priceXAmount = Shopping.get_pricexAmount_product(shopping)

    return render(request, "shopping_cart.html",
            {
                'shopping_cart': shopping,
                'amount' : amount,
                'priceProduct' : priceXAmount
            })



''' Falta poder editar la direccion de usuario '''
def finish_purchase(request):
    if not request.user.is_authenticated():
        return redirect('login')

    address = AddressUser.objects.get(idUser=3, addressDefault=True)
    shopping = Shopping.get_products(request.user)
    totalPrice = Shopping.get_amount(request.user)
    return render(request, "finish_purchase.html",
            {
                'user' : request.user,
                'address' : address,
                'shopping' : shopping,
                'total' : totalPrice
            })