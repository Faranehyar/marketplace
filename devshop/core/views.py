from django.shortcuts import render
from store.models import Product , Category
# Create your views here.

def frontpage (request):
    products = Product.objects.all()[:6]
    categories=Category.objects.all()[:6]
    return render(request, 'core/frontpage.html', {
        'products' : products ,
        'categories' : categories
    })


def about(request):
    return render(request, 'core/about.html')