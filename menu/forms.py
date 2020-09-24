from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import PasswordInput, TextInput, Textarea, CheckboxInput, NullBooleanSelect, RadioSelect, EmailInput, ClearableFileInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm

class ChangeInfoForm(forms.Form):
    new_username = forms.CharField(widget=TextInput(attrs={'placeholder': 'New username'}))

    new_name = forms.CharField(max_length=90, widget=TextInput(attrs={'placeholder': 'New name'}))
    new_email = forms.EmailField(required=False, widget=EmailInput(attrs={'placeholder': 'New email (leave blank to remove)'}))
    new_bio = forms.CharField(required=False, widget=Textarea(attrs={'placeholder': 'New bio (leave blank to remove)'}))
    new_default_city = forms.CharField(max_length=80, required=False)
    new_user_image = forms.ImageField(required=False)
    new_website = forms.CharField(max_length=160, required=False, widget=TextInput(attrs={'placeholder': 'New website (leave blank to remove)'}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ChangeInfoForm, self).__init__(*args, **kwargs)

    def clean_new_username(self):
        new_username = self.cleaned_data['new_username']
        if new_username == '':
            self.add_error('new_username', ValidationError('Please enter a new username or leave as-is'))#, code='none_selected')
            return None
        elif User.objects.exclude(id=self.user.id).filter(username=new_username).exists():
            self.add_error('new_username', ValidationError('New username is already in use'))#, code='none_selected')
        else:
            return new_username

    def clean_new_name(self):
        new_name = self.cleaned_data['new_name']
        if new_name == '':
            self.add_error('new_name', ValidationError('Please enter a new name or leave as-is'))#, code='none_selected')
            return None
        else:
            return new_name

    def clean_new_email(self):
        new_email = self.cleaned_data['new_email']
        if new_email == '':
            return None
        else:
            return new_email

    def clean_bio(self):
        new_bio = self.cleaned_data['new_bio']
        if new_bio == '':
            return None
        else:
            return new_bio

    def clean_new_default_city(self):
        new_default_city = self.cleaned_data['new_default_city']
        if new_default_city == '' or new_default_city == 'null':
            self.add_error('new_default_city', ValidationError('Please select a new city or leave as-is'))#, code='none_selected')
            return None
        else:
            return new_default_city

    def clean_new_website(self):
        new_website = self.cleaned_data['new_website']
        if new_website == '':
            return None
        else:
            return new_website

class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'New password'}))
    new_password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm new password'}))
