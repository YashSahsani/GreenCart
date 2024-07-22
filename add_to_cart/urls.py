from django.urls import path
from . import views

app_name = 'add_to_cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increment/<int:cart_item_id>/', views.increment_quantity, name='increment_quantity'),
    path('decrement/<int:cart_item_id>/', views.decrement_quantity, name='decrement_quantity'),
    path('add_to_wishlist/<int:cart_item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('remove_from_wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add_to_wishlist/product/<int:product_id>/', views.add_to_wishlist, name='add_product_wishlist'),
    path('add_from_wishlist/<int:product_id>/', views.add_to_cart_from_wishlist, name='add_to_cart_from_wishlist'),
]