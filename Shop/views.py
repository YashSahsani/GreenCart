from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from userprofile.models import UserProfile

# Create your views here.
@login_required
def home(request):
    query = request.GET.get('query', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 1000000)
    min_rating = request.GET.get('min_rating', 0)
    sort_by = request.GET.get('sort_by', '')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)
    
    if min_rating:
        products = products.filter(rating__gte=min_rating)  
        
    if sort_by == 'expiry_asc':
        products = products.order_by('expiry')
    elif sort_by == 'expiry_desc':
        products = products.order_by('-expiry')        

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

@login_required
def product_list(request):
    user = request.user
    products = Product.objects.filter(user_id=user.id)
    return render(request, 'Shop/product_list.html', {'products': products,'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

def about(request):
    return render(request, 'about.html',{'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url} )

def privacy_policy(request):
    return render(request, 'FooterPages/privacy_policy.html',{'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

def terms_and_conditions(request):
    return render(request, 'FooterPages/terms_conditions.html',{'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

def gardening_guides(request):
    return render(request, 'FooterPages/gardening_guides.html',{'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

def plant_care_tips(request):
    return render(request, 'FooterPages/plant_care_tips.html',{'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})