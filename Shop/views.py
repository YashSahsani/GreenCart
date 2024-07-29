from datetime import datetime
import pytz
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Product, Reviews
from .forms import ProductForm, ReviewForm
from django.shortcuts import render, redirect
from userprofile.models import UserProfile


def navbar(request):
    if request.user.is_authenticated:
        return render(request, 'navbar.html',
                      {'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})
    else:
        return render(request, 'Dashboard/navbar.html')


@login_required
def home(request):
    ### Retrieving Query Parameters
    query = request.GET.get('query', '')
    min_price = request.GET.get('min_price', 0)
    max_price = request.GET.get('max_price', 1000000)
    min_rating = request.GET.get('min_rating', 0)
    sort_by = request.GET.get('sort_by', '')

    ### Initial Product Query

    products = Product.objects.filter(expiry_date__gte=datetime.now(), in_stock=True)
    
    ### Greeting Message based on time
    timezone = pytz.timezone('America/New_York')
    current_hour = datetime.now(timezone).hour
    if current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    ### User Name
    user_name = request.user.first_name

    ### Handling Search History
    # Retrieves the search history from cookies and splits it into a list.
    search_history = request.COOKIES.get('search_history', '')
    search_history = search_history.split(',') if search_history else []

    ### Filtering Products Based on Query
    if query:
        products = products.filter(name__icontains=query)
        # Store the search query in cookies
        if query not in search_history:
            search_history.append(query)
            search_history_cookie = ','.join(search_history)
        else:
            search_history_cookie = ','.join(search_history)

    ### Filtering Products Based on Price and Rating
    if min_price:
        products = products.filter(discount_price__gte=min_price)

    if max_price:
        products = products.filter(discount_price__lte=max_price)

    if min_rating:
        products = products.filter(rating__gte=min_rating)

    ### Sorting Products based on expiry date
    if sort_by == 'expiry_asc':
        products = products.order_by('expiry')
    elif sort_by == 'expiry_desc':
        products = products.order_by('-expiry')


    response = render(request, 'Shop/home.html', {
        'products': products,
        'greeting': greeting,
        'user_name': user_name,
        'title': 'GreenCart | Home',
        'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url,
        'search_history': search_history,
    })

    ### Set the search history cookie
    if query:
        response.set_cookie('search_history', search_history_cookie, max_age=365*24*60*60)  # Cookie expires in one year

    return response

@login_required
def clear_search_history(request):
    response = redirect('Shop:home')
    response.delete_cookie('search_history')
    return response

    
@login_required
def product_detail(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=id)
        # name = request.POST.get('name')
        review = request.POST.get('review')
        rating = request.POST.get('rating')
        if str.strip(review) and rating:
            Reviews.objects.create(product=product,user= request.user, review=review, rating=rating)
            reviews = Reviews.objects.filter(product=product)
            cal_rating = 0
            if reviews:
                for review in reviews:
                    cal_rating += review.rating
                cal_rating = round(cal_rating / len(reviews), 1)
                product.rating = float(cal_rating)
                product.save()
            return redirect('Shop:product_detail', id=id)
        else:
            reviews = Reviews.objects.filter(product=product)
            return render(request, 'Shop/product-detail.html',
                          {'product': product, 'reviews': reviews, 'rating': product.rating,
                           'user_profile_pic': UserProfile.objects.get(
                               user=request.user).profile_pic.url})
    else:
        product = get_object_or_404(Product, pk=id)
        reviews = Reviews.objects.filter(product=product)
        return render(request, 'Shop/product-detail.html',
                      {'product': product, 'reviews': reviews, 'rating': product.rating,
                       'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})


@login_required
def product_list(request):
    user = request.user
    products = Product.objects.filter(user_id=user.id)
    return render(request, 'Shop/product_list.html', {'products': products, 'user_profile_pic': UserProfile.objects.get(
        user=request.user).profile_pic.url})


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user_id = request.user.id
            product.created_at = datetime.now()
            product.updated_at = datetime.now()
            product.save()
        return redirect('Shop:product_list')  # Redirect to the product list or another appropriate page
    else:
        form = ProductForm()
    return render(request, 'Shop/create_product.html',
                  {'form': form, 'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})


@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.updated_at = datetime.now()
            product.save()
            return redirect('Shop:product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'Shop/edit_product.html',
                  {'form': form, 'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url,
                   'product': product})


@login_required
def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        product.delete()
        return redirect('Shop:product_list')

@login_required
def manage_reviews(request):
    reviews = Reviews.objects.filter(user=request.user)
    print(reviews)
    return render(request,'Shop/manage-review.html',{'reviews':reviews, 'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    print(review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            cal_product = review.product
            cal_reviews = Reviews.objects.filter(product=cal_product)
            cal_rating = 0
            if cal_reviews:
                for cal_review in cal_reviews:
                    cal_rating += cal_review.rating
                cal_rating = round(cal_rating / len(cal_reviews), 1)
                cal_product.rating = float(cal_rating)
                cal_product.save()
            return redirect("Shop:manage_reviews")
    else:
        form = ReviewForm(instance=review)
    return render(request, 'Shop/edit_review.html', {'form': form,'review_id':review_id, 'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Reviews, id=review_id)
    print(review)
    cal_product = review.product
    review.delete()
    cal_reviews = Reviews.objects.filter(product=cal_product)
    cal_rating = 0
    if cal_reviews:
        for cal_review in cal_reviews:
            cal_rating += cal_review.rating
        cal_rating = round(cal_rating / len(cal_reviews), 1)
        cal_product.rating = float(cal_rating)
        cal_product.save()
    else:
        cal_product.rating = 0
        cal_product.save()
    return redirect('Shop:manage_reviews')