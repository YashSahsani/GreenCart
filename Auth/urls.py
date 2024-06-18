from django.urls import path
from .views import Login, Signup, logout
app_name = 'Auth'

urlpatterns = [
    path('login/',Login.as_view() , name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/', logout, name='logout'),
    # path('forgot-password/', views.forgot_password, name='forgot-password'),
    # path('reset-password/', views.reset_password, name='reset-password'),
    # path('change-password/', views.change_password, name='change-password'),

]
