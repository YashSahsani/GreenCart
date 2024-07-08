from django.shortcuts import render


# Create your views here.
def cart(request):
    return render(request, 'Cart/cart.html')
