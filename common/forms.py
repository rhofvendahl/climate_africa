from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, Textarea, CheckboxInput, NullBooleanSelect, RadioSelect
# from django.utils.translation import gettext_lazy as _

is_organization_choices = {
    # (None, '(select one)'),
    (False, 'myself'),
    (True, 'my organization'),
}
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
    bio = forms.CharField(required=False, widget=Textarea(attrs={'placeholder': 'Bio (optional)'}))
    default_city = forms.CharField(max_length=80, required=False)
    user_image = forms.ImageField(required=False)
    website = forms.CharField(max_length=160, required=False, widget=TextInput(attrs={'placeholder': 'Website (optional)'}))

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
