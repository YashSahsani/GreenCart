from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import AppUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, 'Auth/login.html')
    def post(self, request):
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = AppUser.objects.filter(email=email).first()
            if user:
                if check_password(password, user.password):
                    messages.success(request, 'Login successful')
                    return redirect('Shop:home')
                else:
                    messages.error(request, 'Login failed. Please check your username and password.')
                    return redirect('Auth:login')
            else:
                messages.error(request, 'Login failed. Please check your username and password.')
                return redirect('Auth:login')

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
            AppUser.objects.create(first_name=first_name, last_name=last_name, email=email,
                                    password=make_password(password))
            messages.success(request, 'Account created successfully')
            return redirect('Auth:login')
        else:
            messages.error(request, 'Password and Confirm Password do not match')
            return redirect('Auth:login')


def logout(request):
    return HttpResponse("Logout successful")