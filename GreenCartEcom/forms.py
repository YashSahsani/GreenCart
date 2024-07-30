from django import forms
from GreenCartEcom.models import Email


class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']