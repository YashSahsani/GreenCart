# Support/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage, FAQ, Complaint
from django.utils import timezone

@login_required
def chat(request):
    messages = ChatMessage.objects.all().order_by('timestamp')
    return render(request, 'support/chat.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        if message:
            ChatMessage.objects.create(user=request.user, message=message)
            return redirect('support:chat')
    return redirect('support:chat')  # Redirect to chat page after sending message

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
