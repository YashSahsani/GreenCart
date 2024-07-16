from django.contrib import admin
from django.urls import path
from payments.views import payment_view, payment_success, payment_failed, order_summary

app_name='payments'
urlpatterns = [
    path('payment/', payment_view, name='payment_form'),
    path('order/<int:payment_id>/', order_summary, name='order_view'),
    path('success/', payment_success, name='payment_success'),
    path('failed/', payment_failed, name='payment_failed'),
]
