# forms.py

from django import forms
from .models import Query

from .models import Query
class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['first_name', 'last_name', 'email', 'type', 'description', 'attachment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email'}),
            'type': forms.Select(attrs={'class': 'form-dropdown'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Description', 'rows': 5}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-file'}),
        }