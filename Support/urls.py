# Support/urls.py

from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'support'

urlpatterns = [
    path('submit-query/', views.query_form, name='submit_query'),
    path('query-success/', TemplateView.as_view(template_name='support/query_success.html'), name='query_success'),
    # path('send-message/', views.send_message, name='send_message'),
    path('faq/', views.faq, name='faq'),
]
