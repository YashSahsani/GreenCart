from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile
# Create your views here.
@login_required
def home(request):
    return render(request, 'Shop/home.html', {'title': 'GreenCart | Home','user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})
