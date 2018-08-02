from django import forms
from django.core import validators
from .models import Beer

from django.contrib.auth.models import User


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
class UserForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    passwordconfirm = forms.CharField(label="Password confirmation", widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','username','email','password','passwordconfirm')
