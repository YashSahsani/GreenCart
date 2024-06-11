from django.urls import path
from . import views

app_name = 'Auth'

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('signup/', views.signup, name='register'),
    # path('logout/', views.logout, name='logout'),
    # path('forgot-password/', views.forgot_password, name='forgot-password'),
    # path('reset-password/', views.reset_password, name='reset-password'),
    # path('change-password/', views.change_password, name='change-password'),

]
