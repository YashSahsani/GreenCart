from django.urls import path
from .views import Signup, Login, logout_view
app_name = 'Auth'

urlpatterns = [
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
