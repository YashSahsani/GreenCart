from django.urls import path
from . import views

app_name = 'add_to_cart'

urlpatterns = [
    path('', views.cart, name='cart'),
]
