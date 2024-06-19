from django.shortcuts import render
from .models import navCategories


def index(request):
    categoryList = navCategories.objects.all()
    return render(request, 'Dashboard/index.html', {'navCategories': categoryList})

def contact(request):
    return render(request, 'Dashboard/contact.html')

