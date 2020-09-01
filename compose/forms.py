from django import forms
from django.forms.widgets import TextInput, Textarea

class PostForm(forms.Form):
    title = forms.CharField(widget=TextInput(attrs={'placeholder': 'Title'}))
    text = forms.CharField(widget=Textarea(attrs={'placeholder': 'Text'}))
    tags = forms.CharField(max_length=800)
