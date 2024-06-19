from django.shortcuts import render, redirect
from django.views import View
from .models import AppUser
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
from .helper import getSecondsOfOneYear, login_required



class Login(View):
    def get(self, request):
        loginForm = LoginForm()
        return render(request, 'Auth/login.html', {'form': loginForm})

    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            messages.error(request, 'Please check your inputs')
            return redirect('Auth:login')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        remember_me = form.cleaned_data.get('remember_me')
        user = AppUser.objects.get(email=email)
        if user is not None:
            if check_password(password, user.password):
                if remember_me:
                    request.session.set_expiry(getSecondsOfOneYear())  # Set session expiry to 1 year
                else:
                    request.session.set_expiry(0)  # Session expires when the browser is closed
                response = redirect('Shop:home')
                messages.success(request, 'Login successful')
                return response
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
            return redirect('Auth:signup')

@login_required
def logout_view(request):
    request.session.flush()
    messages.warning(request, 'You have been logged out')
    return redirect('/')
