# Support/views.py

from django.contrib.auth.decorators import login_required
from .models import Query, FAQ, TicketStatus
from django.shortcuts import render, redirect, get_object_or_404
from .forms import QueryForm, UpdateStatusForm, TicketInputForm ,TicketNumberForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required


def support_home(request):
    return render(request, 'support/support.html')

def update_sucess(request):
    return render(request, 'support/update_success.html')

def query_sucess(request):
    return render(request, 'support/query_success.html')


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
    form = TicketNumberForm()

    if request.method == 'POST':
        form = TicketNumberForm(request.POST)
        if form.is_valid():
            ticket_number = form.cleaned_data['ticket_number']
            try:
                query = Query.objects.get(ticket_number=ticket_number)
            except Query.DoesNotExist:
                error = "Ticket number not found."

    return render(request, 'support/track_ticket.html', {'form': form, 'query': query, 'error': error})

def ticket_input(request):
    if request.method == 'POST':
        form = TicketInputForm(request.POST)
        if form.is_valid():
            ticket_number = form.cleaned_data['ticket_number']
            return redirect(f'/support/update-status/{ticket_number}/')
    else:
        form = TicketInputForm()

    return render(request, 'support/ticket_input.html', {'form': form})

@staff_member_required
def update_status(request, ticket_number):
    query = get_object_or_404(Query, ticket_number=ticket_number)
    form = UpdateStatusForm(initial={'status': query.statuses.last().status if query.statuses.exists() else ''})

    if request.method == 'POST':
        form = UpdateStatusForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data['status']
            TicketStatus.objects.create(query=query, status=new_status, updated_by=request.user)
            context = {
                'ticket_number': ticket_number,
                'new_status': new_status,
            }
            return render(request, 'support/update_success.html', context)

    return render(request, 'support/update_status.html', {'form': form, 'query': query})

@login_required
def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'support/faq.html', {'faqs': faqs})

