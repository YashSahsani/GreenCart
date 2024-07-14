from django.urls import path
from . import views

app_name = 'GreenCartEcom'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('gardening-guides/', views.gardening_guides, name='gardening_guides'),
    path('plant-care-tips/', views.plant_care_tips, name='plant_care_tips'),
    path('subscribe/', views.subscribe, name='subscribe'),
    
]