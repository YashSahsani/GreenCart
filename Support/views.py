# Support/views.py

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
            query_instance = form.save()

            # Send email to support team
            subject = f"New Query: {query_instance.type} - {query_instance.first_name} {query_instance.last_name}"
            message = (
                f"A new query has been submitted:\n\n"
                f"Type: {query_instance.get_type_display()}\n"
                f"Name: {query_instance.first_name} {query_instance.last_name}\n"
                f"Email: {query_instance.email}\n"
                f"Description: {query_instance.description}"
            )
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['support@greencart.com']  # Replace with actual support email

            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return redirect('query_success.html')  # Redirect to a success page
    else:
        form = QueryForm()

    return render(request, 'support/query_form.html', {'form': form})

# @login_required
# def send_message(request):
#     if request.method == 'POST':
#         message = request.POST.get('message', '')
#         if message:
#             ChatMessage.objects.create(user=request.user, message=message)
#             return redirect('support:chat')
#     return redirect('support:chat')  # Redirect to chat page after sending message

@login_required
def faq(request):
    faqs = FAQ.objects.all()
    return render(request, 'support/faq.html', {'faqs': faqs})

@login_required
def raise_complaint(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        description = request.POST.get('description', '')
        if subject and description:
            Complaint.objects.create(user=request.user, subject=subject, description=description)
            return redirect('support:complaint_thanks')
    return render(request, 'support/raise_complaint.html')

@login_required
def complaint_thanks(request):
    return render(request, 'support/complaint_thanks.html')
