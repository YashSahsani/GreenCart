from django.shortcuts import render, redirect, get_object_or_404
from Shop.models import Product
from userprofile.models import UserProfile
from .models import CartItem, WishlistItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(product__expiry_date__gte=datetime.now(), user_id=request.user.id)
    total_amount = sum(item.total_price() for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)
    return render(request, 'Cart/cart.html',
                  {'cart_items': cart_items, 'total_amount': total_amount, 'total_items': total_items,
                   'user_profile_pic': UserProfile.objects.get(user=request.user).profile_pic.url})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.user_id = request.user.id
    cart_item.save()
    messages.success(request, 'Product added to cart')
    return redirect('Shop:home')


@login_required
def add_to_cart_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.user_id = request.user.id
    cart_item.save()
    messages.success(request, 'Product added to cart')
    return redirect('add_to_cart:wishlist')


@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('add_to_cart:cart')


@login_required
def increment_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('add_to_cart:cart')


@login_required
def decrement_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('add_to_cart:cart')


@login_required
def add_to_wishlist(request, cart_item_id=None, product_id=None):
    global cart_item
    if cart_item_id:
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        product = cart_item.product
    elif product_id:
        product = get_object_or_404(Product, id=product_id)
    else:
        messages.error(request, 'Invalid operation.')
        return redirect('Shop:home')

    # Check if the product is already in the wishlist
    if WishlistItem.objects.filter(product=product, user_id=request.user.id).exists():
        messages.success(request, 'Product is already in your wishlist')
    else:
        WishlistItem.objects.create(product=product, user_id=request.user.id)
        messages.success(request, 'Product added to wishlist')

        if cart_item_id:
            cart_item.delete()
            return redirect('add_to_cart:cart')

    return redirect('Shop:home')


@login_required
def wishlist_view(request):
    wishlist_items = WishlistItem.objects.filter(product__expiry_date__gte=datetime.now(), user_id=request.user.id)
    return render(request, 'Cart/wishlist.html', {'wishlist_items': wishlist_items,
                                                  'user_profile_pic': UserProfile.objects.get(
                                                      user=request.user).profile_pic.url})


@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id)
    wishlist_item.delete()
    return redirect('add_to_cart:wishlist')
