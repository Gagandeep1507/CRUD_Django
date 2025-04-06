from django import forms
from .models import User

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }