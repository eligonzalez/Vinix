from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

''' Necesito los productos del carrito (nombre, cantidadProducto, precio, etc)
    Necesito el objeto carrito (compraTotal)'''

''' Falta comprobar que los términos y condiciones este chekeado '''
def shopping_cart(request):
    if not request.user.is_authenticated():
        return redirect('login')

    sc = Shopping_Cart.get_products(user=request.user)
    amount = Shopping_Cart.get_amount(user=request.user)

    return render(request, "shopping_cart.html",
            {
                'shopping_cart': sc,
                'amount' : amount,
            })


''' Necesito el objeto user (nombre, email)
    Necesito el objeto direccionUsuario (calle, poblacion, codigoPostal)
    Necesito los objetos ProductosCarrito (imagen, cantidad, nombreProducto)
    Necesito el objeto carrito (compraTotal) '''

''' Falta poder editar la direccion de usuario '''
def finish_purchase(request):
    if not request.user.is_authenticated():
        return redirect('login')

    return render(request, "finish_purchase.html", {})