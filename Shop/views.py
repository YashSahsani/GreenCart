from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Shop.models import Product
from userprofile.models import UserProfile
# Create your views here.
@login_required
def home(request):
    return render(request, 'Shop/home.html', {'title': 'GreenCart | Home','user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

def product_detail(request,id):
    product = Product.objects.get(id=id)
    return render(request,'Shop/product-detail.html',{'name':product.name,'description':product.description,'price':product.price,'expiry':product.expiry})