from django.shortcuts import render
from django.views import View


# Create your views here.
def cart(request):
    return render(request, 'Cart/base.html')
