from django.shortcuts import render
from products.models import Product
from marketplaces.models import Marketplace

def index(request):
    products = Product.objects.all()
    marketplaces = Marketplace.objects.all()
    return render(
        request,
        'index.html',
        {
            'products': products,
            'marketplaces': marketplaces,
        }
    )
