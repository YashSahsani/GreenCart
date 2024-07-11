from django.contrib import admin

# Register your models here.
from .models import navCategories, offer

admin.site.register(navCategories)
admin.site.register(offer)
