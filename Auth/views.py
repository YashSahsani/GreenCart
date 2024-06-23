from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm, ForgotPasswordForm, ResetPasswordForm
from .backend import getSecondsOfOneYear
from .models import User
from django.urls import reverse



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
            messages.success(request, 'Welcome '+str(user.first_name)+'!')
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
        if form.is_valid():
            form.save()
            messages.success(request, str(form.cleaned_data.get('first_name'))+' account has been created successfully. Please login to continue.')
            return redirect('Auth:login')
        else:
            messages.error(request, 'Please check your inputs')
            return redirect('Auth:signup')
        

def forgot_password(request):
    form = ForgotPasswordForm()
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = User.objects.filter(email=email).first()
            if user:
                return redirect(reverse('Auth:reset_password') + f'?email={email}')

    return render(request, 'Auth/forgot_password.html', {'form': form})

def reset_password(request):
    email = request.GET.get('email')
    if not email:
        messages.error(request, 'Invalid password reset link.')
        return redirect('forgot_password')
    if request.method == 'POST':
        form = ResetPasswordForm(request.POST, email=email)
        if form.is_valid():
            user = User.objects.filter(email=email).first()
            if user:
                user.set_password(form.cleaned_data['password1'])
                user.save()
                messages.success(request, 'Your password has been successfully reset.')
                return redirect(reverse('Auth:login'))
    else:
        form = ResetPasswordForm(email=email)

    return render(request, 'Auth/reset_password.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    request.session.flush()
    messages.warning(request, 'You have been logged out')
    return redirect('/')
