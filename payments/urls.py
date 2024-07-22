from django.contrib import admin
from django.urls import path
from payments.views import payment_view, payment_success, payment_failed, order_summary, checkout

app_name = 'payments'
urlpatterns = [
    path('payment/', payment_view, name='payment_form'),
    path('order/<int:payment_id>/', order_summary, name='order_view'),
    path('checkout/<int:payment_id>/', checkout, name='checkout'),
    path('success/', payment_success, name='payment_success'),
    path('failed/<int:payment_id>/', payment_failed, name='payment_failed'),
]