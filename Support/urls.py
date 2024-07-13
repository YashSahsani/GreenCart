# Support/urls.py

from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'support'

urlpatterns = [
    path('submit-query/', views.query_form, name='submit_query'),
    path('query-success/', TemplateView.as_view(template_name='support/query_success.html'), name='query_success'),
    path('track-ticket/', views.track_ticket, name='track_ticket'),
    path('update-status/<int:ticket_number>/', views.update_status, name='update_status'),
    path('update-success/', TemplateView.as_view(template_name='support/update_success.html'), name='update_success'),
    path('faq/', views.faq, name='faq'),
]
