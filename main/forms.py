from .models import Contact
from django import forms
from django.forms import ModelForm, TextInput, EmailInput,CharField

class contactform(forms.ModelForm):
    class Meta:
        model=Contact
        # fields=['name','email']
        fields="__all__"
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control mb-3",
                'style': 'max-width: 100%;',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control mb-3",
                'style': 'max-width: 100%;',
                'placeholder': 'Your Email'
            }),

            'sub': TextInput(attrs={
                'class': "form-control mb-3",
                'style': 'max-width: 100%;',
                'placeholder': 'Your Subject'
            }),
            'msg': TextInput(attrs={
                'class': "form-control mb-3",
                'style': 'max-width: 100%;',
                'placeholder': 'Your Message'
            }),

        }