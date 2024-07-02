from django.shortcuts import render, redirect
from .forms import PaymentForm


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payments:payment_success')  # Ensure 'payment_success' matches the name in urls.py
    else:
        form = PaymentForm()

    return render(request, 'payments/payment_form.html', {'form': form})


def payment_success(request):
    return render(request, 'payments/payment_success.html')
