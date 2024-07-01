from django.urls import path
from .views import get_user_details, edit_user_details

app_name = 'userprofile'

urlpatterns = [
    path('get_user_details/', get_user_details, name='get_user_details'),
    path('edit_user_details/', edit_user_details, name='edit_user_details'),
]