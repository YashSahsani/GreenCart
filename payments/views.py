from django.conf import settings
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import PaymentForm
from .models import Payment
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_view(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment_intent = stripe.PaymentIntent.create(
                amount=int(payment.Amount * 100),  # Stripe expects the amount in cents
                currency='cad',
                metadata={'email': payment.Email}
            )
            payment.stripe_payment_intent_id = payment_intent['id']
            payment.save()
            return render(request, 'payments/checkout.html', {
                'payment_intent_client_secret': payment_intent['client_secret'],
                'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
                'payment': payment
            })
    return render(request, 'payments/payment_form.html', {'form': form})


def payment_success(request):
    return render(request, 'payments/payment_success.html')
