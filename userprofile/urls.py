from django.urls import path
from .views import get_user_details, add_user_details

app_name = 'userprofile'

urlpatterns = [
    path('get_user_details/', get_user_details, name='get_user_details'),
    path('add_user_details/', add_user_details, name='add_user_details'),
]