# forms.py

from django import forms
from .models import Query

from .models import Query, TicketStatus, faqCategory
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
            'attachment': forms.FileInput(attrs={'class': 'form-file'}),
        }
class TicketNumberForm(forms.Form):
    ticket_number = forms.CharField(
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Enter Ticket Number'}),
        required=True
    )
class TicketInputForm(forms.Form):
    ticket_number = forms.IntegerField(
        label='Ticket Number',
        max_value=9999999999,
        widget=forms.TextInput(attrs={'placeholder': 'Enter Ticket Number Here!', 'maxlength': '10'})
    )

class UpdateStatusForm(forms.Form):
    status = forms.ChoiceField(
        choices=TicketStatus.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-dropdown'}),
        required=True
    )

class FAQSearchForm(forms.Form):
    query = forms.CharField(label='Type your Question Here:', max_length=255, required=False)
    category = forms.ModelChoiceField(queryset=faqCategory.objects.all(), label='Category', required=False)