from django.urls import path
from . import views

app_name = 'add_to_cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increment/<int:cart_item_id>/', views.increment_quantity, name='increment_quantity'),
    path('decrement/<int:cart_item_id>/', views.decrement_quantity, name='decrement_quantity'),
]