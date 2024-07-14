from django.shortcuts import redirect, render
from django.urls import reverse

from userprofile.models import UserProfile
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
    
        # Redirect to the success page
        return render(request, 'FooterPages/subscription_success.html')
    return redirect(reverse('home'))