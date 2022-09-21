from django import forms
from django.forms import ModelForm
from .models import Profile

STATE = [
    ("Abia","Abia"),
    ("Adamawa","Adamawa"),
    ("Enugu","Enugu"),
    ("Lagos","Lagos"),
    ("Lagos","Lagos"),
    ("Ondo","Ondo"),
]
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name','email','phone','address','city','state','profile_pix']
        Widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name is required'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name is required'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email is required'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone number is required'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your address is required'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'city'}),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'state'}, choices=STATE),
            'profile_pix': forms.FileInput(attrs={'class': 'form-control'}),
            
        }    