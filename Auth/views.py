from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, 'Auth/login.html')
    def post(self, request):
            pass

class Signup(View):
    def get(self, request):
        return render(request, 'Auth/signup.html')
    def post(self, request):
        print(request.POST)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            User.objects.create(username=email, first_name=first_name, last_name=last_name, email=email,
                                    password=make_password(password))
            return HttpResponse("Signup successful")
        else:
            return HttpResponse("Passwords do not match")