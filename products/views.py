from django.shortcuts import render
from . models import *

def list_products(request):
    all_products = Products.objects.all()
    context = {
        'products': all_products,
    }
    return render(request, 'home.html', context)

def view_products(request):
    products = Products.objects.all()
    categories = Catagories.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products.html', context)


