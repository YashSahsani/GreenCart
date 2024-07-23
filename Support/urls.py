# Support/urls.py

from django.urls import path
from . import views


app_name = 'support'

urlpatterns = [
    path('', views.support_home, name='support-home'),
    path('submit-query/', views.query_form, name='submit_query'),
    path('query-success/', views.query_sucess, name='query_success'),
    path('track-ticket/', views.track_ticket, name='track_ticket'),
    path('ticket-input/', views.ticket_input, name='ticket_input'),
    path('update-status/<int:ticket_number>/', views.update_status, name='update_status'),
    path('update-success/', views.update_sucess, name='update_success'),
    path('faq/', views.faq, name='faq'),
]
