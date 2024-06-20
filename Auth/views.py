from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from .backend import getSecondsOfOneYear



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
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            if remember_me:
                request.session.set_expiry(getSecondsOfOneYear())
            else:
                request.session.set_expiry(0)
            messages.success(request, 'You have been logged in')
            return redirect('Shop:home')
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
            return redirect('Auth:login')

class Signup(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'Auth/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)
        print("form:"+str(form.is_valid()))
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('Auth:login')
        else:
            print(form.errors)
            messages.error(request, 'Please check your inputs')
            return redirect('Auth:signup', {'form': form})
        

@login_required
def logout_view(request):
    logout(request)
    request.session.flush()
    messages.warning(request, 'You have been logged out')
    return redirect('/')
