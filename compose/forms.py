from django import forms
from django.forms.widgets import TextInput, Textarea, ClearableFileInput
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.Form):
    title = forms.CharField(widget=TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(widget=Textarea(attrs={'placeholder': 'Text'}))
    tags = forms.CharField(max_length=800)
    city = forms.CharField(max_length=80)
    # image = forms.ImageField(widget=ClearableFileInput(attrs={'class': 'form-control-file'}))
    image = forms.ImageField(required=False)

    def clean_city(self):
        city = self.cleaned_data['city']
        if (not city) or (city == 'null'):
            self.add_error('city', ValidationError('Please select a city from the dropdown'))#, code='none_selected')
        return city
