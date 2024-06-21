from django.contrib import admin
from django.urls import path, include

admin.site.index_title = "Welcome to GreenCart Admin Portal"
admin.site.site_title = "GreenCart Admin Portal"
admin.site.site_header = "GreenCart Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GreenCartEcom.urls','GreenCartEcom'), name='GreenCartEcom'),
    path('auth/', include('Auth.urls','Auth'), name='Auth'),
    path('shop/', include('Shop.urls','Shop'), name='Shop'),
]

