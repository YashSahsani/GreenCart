from django.urls import path
from .views import about, home, privacy_policy, product_detail, product_list, terms_and_conditions, plant_care_tips, gardening_guides, create_product, edit_product, delete_product
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
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),

]

