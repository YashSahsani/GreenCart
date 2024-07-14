from django.contrib import admin
from django.urls import path
from payments.views import payment_view, payment_success

app_name='payments'
urlpatterns = [
    path('payment/', payment_view, name='payment_form'),
    path('success/', payment_success, name='payment_success'),
]
