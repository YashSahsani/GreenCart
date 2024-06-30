from django.urls import path
from .views import home, product_detail
app_name = 'Shop'

urlpatterns = [
    path('',home, name='home'),
    path('cart/',home, name='cart'),
    path('checkout/',home, name='checkout'),
    path('order/',home, name='order'),
    path('profile/',home, name='profile'),
    path('product-detail/<int:id>', product_detail, name='product_detail'),
]
