# forms.py

from django import forms
from .models import Query

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['first_name', 'last_name', 'email', 'type', 'description', 'attachment']
