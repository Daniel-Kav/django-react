from typing import Any
from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' not in title:
            raise ValidationError("we only accept django title")
        return title