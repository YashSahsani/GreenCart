from django.shortcuts import render
from Auth.helper import login_required
# Create your views here.
@login_required
def home(request):
    return render(request, 'Shop/home.html')