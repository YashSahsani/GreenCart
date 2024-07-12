# Support/views.py

from django.contrib.auth.decorators import login_required
from .models import Query, FAQ
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QueryForm
from django.core.mail import send_mail
from django.conf import settings


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
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return render(request, 'support/query_success.html', {'ticket_number': query.ticket_number})
    else:
        form = QueryForm()

    return render(request, 'support/query_form.html', {'form': form})

def track_ticket(request):
    query = None
    error = None
    if request.method == 'POST':
        ticket_number = request.POST.get('ticket_number')
        try:
            query = Query.objects.get(ticket_number=ticket_number)
        except Query.DoesNotExist:
            error = "Ticket number not found."

    return render(request, 'support/track_ticket.html', {'query': query, 'error': error})
@login_required
def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'support/faq.html', {'faqs': faqs})

