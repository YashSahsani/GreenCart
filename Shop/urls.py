from django.urls import path
from .views import clear_search_history, home, product_detail, product_list, create_product, edit_product, delete_product, manage_reviews, delete_review ,edit_review

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
    path('clear_search_history/', clear_search_history, name='clear_search_history'),
    path('manage_reviews/',manage_reviews, name='manage_reviews'),
    path('edit/<int:review_id>/', edit_review, name='edit_review'),
    path('delete/<int:review_id>/', delete_review, name='delete_review'),
]

