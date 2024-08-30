from typing import Any
from django import forms
from django.core.exceptions import ValidationError

from .models import Notes


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            "title": forms.TextInput(attrs = {'placeholder':'Title',"class":"form-control my-5"}),
            'text': forms.Textarea(attrs = {'placeholder':'type your notes here', 'class':'form-control mb-5'}),
        }
        labels = {
            "text": "Description",
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'django' not in title:
            raise ValidationError("we only accept django title")
        return title