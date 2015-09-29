import django_filters
from .models import Product, Wine, Spirit

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ()
        order_by= (
        	('name', 'Nombre'),
            ('-name', 'Nombre descendiente'),
        	('price', 'Precio'),
        	('country', 'País')
        	)

