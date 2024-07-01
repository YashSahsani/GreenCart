from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Admin site configuration
admin.site.index_title = "Welcome to GreenCart Admin Portal"
admin.site.site_title = "GreenCart Admin Portal"
admin.site.site_header = "GreenCart Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('GreenCartEcom.urls', 'GreenCartEcom'), name='GreenCartEcom'),
    path('cart/', include('add_to_cart.urls', 'AddToCart'), name='AddToCart'),
    path('auth/', include('Auth.urls', 'Auth'), name='Auth'),
    path('shop/', include('Shop.urls', 'Shop'), name='Shop'),
    path('profile/', include('userprofile.urls', 'Profile'), name='Profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
