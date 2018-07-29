from django import forms
from django.core import validators
from .models import Beer

class NewBeer(forms.ModelForm):
    class Meta():
        model = Beer
        fields = '__all__'

class SearchBeer(forms.ModelForm):
    class Meta():
        model = Beer
        fields = [
            'alcoholVolume',
            'brand',
            'bodyType',
            'containerType',
            'taste',
        ]
