from django import forms
from django.core.exceptions import ValidationError
from . import util
from . import helpers

class createPage(forms.Form):
    title = forms.CharField(label="title")
    content = forms.CharField(widget=forms.Textarea)

class editPage(forms.Form):
    content = forms.CharField(widget=forms.Textarea)