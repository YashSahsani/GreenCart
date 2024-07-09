# forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name', 'description', 'price', 'expiry',
            'discount_price', 'image', 'in_stock',
            'rating', 'user_id'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'expiry': forms.NumberInput(attrs={'min': 0}),
            'price': forms.NumberInput(attrs={'step': 0.01}),
            'discount_price': forms.NumberInput(attrs={'step': 0.01}),
            'rating': forms.NumberInput(attrs={'step': 0.01, 'min': 0, 'max': 5}),
        }
