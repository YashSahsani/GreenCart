from django.conf import settings
from django.shortcuts import render, redirect
from add_to_cart.models import CartItem
from .models import Order, OrderItem, Payment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import PaymentForm
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


def payment_view(request):
    form = PaymentForm()
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.save()
            return redirect('payments:order_view', payment_id=payment.id)
    return render(request, 'payments/payment_form.html', {'form': form})


def payment_success(request):
    return render(request, 'payments/payment_success.html')


def payment_failed(request):
    return render(request, 'payments/payment_failed.html')


def order_summary(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    cart_items = CartItem.objects.all()
    total_amount = sum(item.total_price() for item in cart_items)
    total_items = sum(item.quantity for item in cart_items)

    if request.method == 'POST':
        order = Order.objects.create(total_amount=total_amount, total_items=total_items, payment=payment)
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product.name,
                quantity=item.quantity,
                price=item.product.price,
            )
        cart_items.delete()  # Clear the cart after creating the order

        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),
            currency='cad',
            metadata={'email': payment.Email}
        )
        payment.stripe_payment_intent_id = payment_intent['id']
        payment.save()

        return render(request, 'payments/checkout.html', {
            'payment_intent_client_secret': payment_intent['client_secret'],
            'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY,
            'order': order,
            'payment': payment,
            'total_amount': total_amount,
        })

    return render(request, 'payments/order_summary.html', {
        'cart_items': cart_items,
        'total_amount': total_amount,
        'total_items': total_items,
        'payment': payment,
    })
