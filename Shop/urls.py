from django.urls import path
from .views import home, product_detail, product_list, about, privacy_policy, terms_and_conditions, gardening_guides, plant_care_tips, create_product, edit_product, delete_product, subscribe

app_name = 'Shop'

urlpatterns = [
    path('',home, name='home'),
    path('cart/',home, name='cart'),
    path('checkout/',home, name='checkout'),
    path('order/',home, name='order'),
    path('profile/',home, name='profile'),
    path('product-detail/<int:id>', product_detail, name='product_detail'),
    path('mylistings/', product_list, name='product_list'),
    path('about/', about, name='about'),
    path('privacy-policy/', privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', terms_and_conditions, name='terms_and_conditions'),
    path('gardening-guides/', gardening_guides, name='gardening_guides'),
    path('plant-care-tips/', plant_care_tips, name='plant_care_tips'),
    path('create_product/', create_product, name='create_product'),
    path('subscribe/', subscribe, name='subscribe'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('delete_product/', delete_product, name='delete_product'),

]

