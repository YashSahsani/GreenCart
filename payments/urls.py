from django.contrib import admin
from django.urls import path
from payments.views import payment_view, payment_success  # Import payment_success from payments.views

app_name='payments'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('payment/', payment_view, name='payment_form'),
    path('success/', payment_success, name='payment_success'),  # Use payment_success from imported module
]
