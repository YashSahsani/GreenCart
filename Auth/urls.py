from django.urls import path
from .views import Signup, Login, logout_view, forgot_password,reset_password
app_name = 'Auth'

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset_password/', reset_password, name='reset_password'),
]
