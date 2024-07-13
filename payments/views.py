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
            try:
                payment_intent = stripe.PaymentIntent.create(
                    amount=int(payment.amount * 100),
                    currency='cad',
                    metadata={'email': payment.email}
                )
                payment.stripe_payment_intent_id = payment_intent['id']
                payment.save()
                return render(request, 'payments/checkout.html', {
                    'payment_intent_client_secret': payment_intent['client_secret'],
                    'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
                    'payment': payment
                })
            except stripe.error.CardError as e:
                form.add_error(None, "Your card was declined.")
            except stripe.error.RateLimitError as e:
                form.add_error(None, "Rate limit error. Please try again.")
            except stripe.error.InvalidRequestError as e:
                form.add_error(None, "Invalid parameters. Please check your input.")
            except stripe.error.AuthenticationError as e:
                form.add_error(None, "Authentication error. Please try again.")
            except stripe.error.APIConnectionError as e:
                form.add_error(None, "Network error. Please try again.")
            except stripe.error.StripeError as e:
                form.add_error(None, "Something went wrong. Please try again later.")
            except Exception as e:
                form.add_error(None, "An error occurred. Please try again.")
    return render(request, 'payments/payment_form.html', {'form': form})

def payment_success(request):
    return render(request, 'payments/payment_success.html')

def payment_failed(request):
    return render(request, 'payments/payment_failed.html')
