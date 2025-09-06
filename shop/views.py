from django.shortcuts import render, HttpResponse
from .models import Product

def helloAdmin(request):
    all_products = Product.objects.all()
    
    return render(request, 'index.html', {'products': all_products})