from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from Shop.models import Product
from userprofile.models import UserProfile
from .models import Product

# Create your views here.
@login_required
def home(request):
    query = request.GET.get('query', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 1000000)

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    current_hour = datetime.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    user_name = request.user.first_name if request.user.is_authenticated else "Guest"

    return render(request, 'Shop/home.html', {'products': products,'greeting': greeting,'user_name': user_name,'title': 'GreenCart | Home','user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

@login_required
def product_detail(request,id):
    product = get_object_or_404(Product, pk=id)
    return render(request,'Shop/product-detail.html',{'name':product.name,'description':product.description,'price':product.price,'expiry':product.expiry,'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

