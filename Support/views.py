# Support/views.py
import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Query, FAQ, Complaint
from django.utils import timezone
from django.shortcuts import render, redirect
from .forms import QueryForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView  # Ensure TemplateView import is correct
from django.urls import reverse_lazy

@login_required
def query_form(request):
    if request.method == 'POST':
        form = QueryForm(request.POST, request.FILES)
        if form.is_valid():
            query = form.save()

            subject = f"New Query: {query.type} - {query.first_name} {query.last_name}"
            message = (
                f"A new query has been submitted:\n\n"
                f"Type: {query.get_type_display()}\n"
                f"Name: {query.first_name} {query.last_name}\n"
                f"Email: {query.email}\n"
                f"Description: {query.description}"
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['support@greencart.com']
            ticket_number = random.randint(10000, 99999)
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return render(request, 'support/query_success.html', {'ticket_number': ticket_number})
    else:
        form = QueryForm()

    return render(request, 'support/query_form.html', {'form': form})


@login_required
def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'support/faq.html', {'faqs': faqs})

