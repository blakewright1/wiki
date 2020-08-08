import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class EditForm(forms.Form):
    edited_page = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20, "value": 'edits here'}), initial='test text')


class CreateForm(forms.Form):
    created_title = forms.CharField()
    created_page = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}), initial='test text')
