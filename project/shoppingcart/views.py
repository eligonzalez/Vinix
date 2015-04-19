from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here
from .models import Shopping_Cart

def shopping_cart(request):
    if not request.user.is_authenticated():
        return redirect('login')

    sc = Shopping_Cart.get_products(user=request.user)
    print(request.user)
    print(sc)
    for item in sc:
        print(item)

    return render(request, "home_view.html",
            {
                'shopping_cart': sc,
            })