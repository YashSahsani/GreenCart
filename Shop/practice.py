# django-admin startproject projectname
# python manage.py startapp appname
# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate





from datetime import datetime
import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Product, Reviews
from .forms import ProductForm, ReviewForm
from django.shortcuts import render, redirect
from userprofile.models import UserProfile

def home (request):
    query = request.GET.get('query', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 1000000)
    min_rating = request.GET.get('min_rating', 0)
    sort_by = request.GET.get('sort_by', '')
    
    
    products = Product.objects.filter(expiry_date__gte=datetime.now(), in_stock=True)
    
    timezone = pytz.timezone('Canada/Toronto')
    current_hour = datetime.now(timezone).hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
        
    user_name = request.user.first_name
    
    search_history = request.COOKIES.get('search_history','')
    search_history = search_history.split(',') if search_history else []
    
    if query:
        products = products.filter(name__icontains=query)
        
        if query not in search_history:
            search_history.append(query)
            search_history_cookie = ','.join(search_history)
        else:
            search_history_cookie = ','.join(search_history)

    if min_price:
        products = products.filter(discount_price__gte=min_price)
        
    if max_price:
        products = products.filter(discount_price__lte=max_price)

    if sort_by == 'expiry_asc':
        products = products.order_by('expiry')
    elif sort_by == 'expiry_desc':
        products = products.order_by('-expiry')
        
    response = render(request, 'Shop/home.html', {
        'products': products,
        'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url,

    })
    
    if query:
        response.set_cookie('search_history', search_history_cookie, max_age=365)
    
    return response


# ------------------------------------------------------------


def clear_search_history(request):
    response = redirect('Shop:home')
    response.delete_cookie('search_history')
    return response

# ------------------------------------------------------------


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']

# ------------------------------------------------------------

def subscribe(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmailForm()
        
    return render(request, 'Footer.html', {'form':form})


# ------------------------------------------------------------

class MyForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
    
def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            # Process form data
            pass
    else:
        form = MyForm()
    return render(request, 'my_template.html', {'form': form})
            
# ------------------------------------------------------------     
             
class MyForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
def my_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            form.save()  # Save the model instance
            return redirect('success')
    else:
        form = MyModelForm()
    return render(request, 'my_template.html', {'form': form})