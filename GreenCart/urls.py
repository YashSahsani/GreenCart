"""
URL configuration for GreenCart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
admin.site.site_header="GreenCart Admin"
admin.site.site_title ="GreenCart Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GreenCartEcom.urls','GreenCartEcom'), name='GreenCartEcom'),
    path('cart/', include('add_to_cart.urls', 'AddToCart'), name='AddToCart'),
    path('auth/', include('Auth.urls','Auth'), name='Auth'),
    path('shop/', include('Shop.urls','Shop'), name='Shop'),
]

