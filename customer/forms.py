from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    address = forms.CharField(required=False)
    phone = forms.CharField(required=False)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password1', 'password2', 'address', 'phone']
