from django.shortcuts import redirect, render
from django.urls import reverse
from datetime import datetime

from userprofile.models import UserProfile
from .models import  offer
from Shop.models import Product

def index(request):
    if request.user.is_authenticated:
        return redirect('Shop:home')  # Redirect to home page if user is already logged in
    # productList = Product.objects.all()
    productList = Product.objects.filter(expiry_date__gte=datetime.now(), in_stock=True)
    offerPosterList = offer.objects.all()
    # Fetch all products
    return render(request, 'Dashboard/index.html', {
        'products': productList,
        'offers': offerPosterList
    })

def contact(request):
    return render(request, 'Dashboard/contact.html')


def about(request):
    if request.user.is_authenticated:
        return render(request, 'about.html', {'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})
    else:
        return render(request, 'about.html')

def privacy_policy(request):
    if request.user.is_authenticated:
        return render(request, 'FooterPages/privacy_policy.html', {'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})
    else:
        return render(request, 'FooterPages/privacy_policy.html')
    

def terms_and_conditions(request):
    if request.user.is_authenticated:
        return render(request, 'FooterPages/terms_conditions.html', {'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})
    else:
        return render(request, 'FooterPages/terms_conditions.html')
    

def gardening_guides(request):
    if request.user.is_authenticated:
        return render(request, 'FooterPages/gardening_guides.html', {'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})
    else:
        return render(request, 'FooterPages/gardening_guides.html')

def plant_care_tips(request):
    if request.user.is_authenticated:
        return render(request, 'FooterPages/plant_care_tips.html', {'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})
    else:
        return render(request, 'FooterPages/plant_care_tips.html')
    

def subscribe(request):
    if request.method == "POST":
    
        return render(request, 'FooterPages/subscription_success.html')
    return redirect(reverse('home'))