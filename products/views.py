from django.shortcuts import render
from . models import *

def list_products(request):
    all_products = Products.objects.all()
    context = {
        'products': all_products,
    }
    return render(request, 'home.html', context)


