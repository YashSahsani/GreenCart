from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
from .models import Product

# Create your views here.
@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'Shop/home.html',{'products': products,'title': 'GreenCart | Home','user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'Shop/product_detail.html', {'product': product})