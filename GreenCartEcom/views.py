from django.shortcuts import render
from .models import navCategories, offer
from Shop.models import Product

def index(request):
    categoryList = navCategories.objects.all()
    productList = Product.objects.all()  
    offerPosterList = offer.objects.all()
    # Fetch all products
    return render(request, 'Dashboard/index.html', {
        'navCategories': categoryList,
        'products': productList,
        'offers': offerPosterList
         # Pass products to the template
    })

def contact(request):
    return render(request, 'Dashboard/contact.html')
