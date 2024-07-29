from django.contrib import admin

# Register your models here.
from .models import  Email, offer

admin.site.register(offer)
admin.site.register(Email)