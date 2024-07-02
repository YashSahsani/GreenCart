from django import forms
from Auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'date_of_birth', 'address_line_1', 'address_line_2', 'city', 'state', 
            'country', 'zip_code', 'phone_number', 'profile_pic', 'location'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'address_line_1': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'address_line_2': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'city': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'state': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'country': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'zip_code': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'location': forms.TextInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full',
                'readonly': 'readonly'
            }),
            'profile_pic': forms.FileInput(attrs={
                'class': 'editable-field bg-transparent border-none text-center w-full'
            }),
        }
