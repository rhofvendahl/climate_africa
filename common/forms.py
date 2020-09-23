from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, Textarea, CheckboxInput, NullBooleanSelect, RadioSelect, EmailInput, ClearableFileInput
# from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

is_organization_choices = [
    (None, '(select one)'),
    (False, 'myself'),
    (True, 'my organization'),
]
#
# class CustomNullBooleanSelect(NullBooleanSelect):
#     def __init__(self, attrs=None):
#         choices = (
#             ('unknown', _('(select one)')),
#             ('true', _('my organization')),
#             ('false', _('myself')),
#         )
#         super().__init__(attrs, choices)

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Confirm password'}))

    is_organization = forms.ChoiceField(choices=is_organization_choices)#widget=CustomNullBooleanSelect())#(choices=is_organization_choices))#widget=CheckboxInput(attrs={'class': 'form-check-input'}))
    name = forms.CharField(max_length=90, widget=TextInput(attrs={'placeholder': 'Name'}))
    email = forms.EmailField(required=False, widget=EmailInput(attrs={'placeholder': 'Email (optional)'}))
    bio = forms.CharField(required=False, widget=Textarea(attrs={'placeholder': 'Bio (optional)'}))
    default_city = forms.CharField(max_length=80, required=False)
    user_image = forms.ImageField(required=False)
    website = forms.CharField(max_length=160, required=False, widget=TextInput(attrs={'placeholder': 'Website (optional)'}))

    def clean_is_organization(self):
        is_organization = self.cleaned_data['is_organization']
        if is_organization == 'None':
            self.add_error('is_organization', ValidationError('Please select who this profile is for'))#, code='none_selected')
            return None
        elif is_organization == 'True':
            return True
        elif is_organization == 'False':
            return False
        print('Error: unexpected is_organization value')
        return is_organization

    def clean_bio(self):
        bio = self.cleaned_data['bio']
        if bio == '':
            return None
        else:
            return bio

    def clean_default_city(self):
        default_city = self.cleaned_data['default_city']
        print('PRE DEFAULT CITY', default_city)
        if default_city == '' or default_city == 'null':
            self.add_error('default_city', ValidationError('Please select a default city from the dropdown'))#, code='none_selected')
            return None
        else:
            return default_city

    def clean_website(self):
        website = self.cleaned_data['website']
        if website == '':
            return None
        else:
            return website

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
