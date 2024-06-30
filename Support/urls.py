# Support/urls.py

from django.urls import path
from . import views

app_name = 'support'

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    path('send-message/', views.send_message, name='send_message'),
    path('faq/', views.faq, name='faq'),
    path('raise-complaint/', views.raise_complaint, name='raise_complaint'),
    path('complaint-thanks/', views.complaint_thanks, name='complaint_thanks'),
]
