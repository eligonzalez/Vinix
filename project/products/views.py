#Django Imports
from django.shortcuts import render
from django.contrib import admin
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#Util Imports


#Project Imports
from .models import Wine, Product
# Create your views here.

admin.autodiscover()

def home_view(request):
    wines = Wine.objects.all().order_by('?')[:12]
    paginator = Paginator(wines, 4)
    page = request.GET.get('page')

    try:
        prod_page = paginator.page(page)
    except PageNotAnInteger:
        prod_page = paginator.page(1)
    except EmptyPage:
         prod_page = paginator.page(paginator.num_pages)

    return render(request,'home_view.html',
        {
            'products': wines,
            'list_prod': prod_page
        }
    )

def wine_view(request, wine_id):
    wine_data = get_object_or_404(Wine, pk=wine_id)
    return render(request,'wine_view.html',
        {
            'wine_data': wine_data,
        }
    )