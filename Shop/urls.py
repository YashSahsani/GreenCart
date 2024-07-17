from django.urls import path
from .views import home, product_detail, product_list, create_product, edit_product, delete_product

app_name = 'Shop'

urlpatterns = [
    path('',home, name='home'),
    path('cart/',home, name='cart'),
    path('checkout/',home, name='checkout'),
    path('order/',home, name='order'),
    path('profile/',home, name='profile'),
    path('product-detail/<int:id>', product_detail, name='product_detail'),
    path('mylistings/', product_list, name='product_list'),
    path('create_product/', create_product, name='create_product'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('delete_product/', delete_product, name='delete_product'),

]

