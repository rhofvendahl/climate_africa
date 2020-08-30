from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm password'}))

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
