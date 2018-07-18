from django import forms
from django.core import validators
from .models import Beer

class NewBeer(forms.ModelForm):
    class Meta():
        model = Beer
        fields = '__all__'

# class FormName(forms.Form):
#     name = forms.CharField()
#     origin = forms.CharField()
#     acl = forms.DecimalField()
#     photo = forms.ImageField()
#     details = forms.CharField(widget=forms.Textarea)



    # def clean(self):
    #     all_clean_data = super().clean()
    #     name = all_clean_data['name']
    #     origin = all_clean_data['origin']
    #     acl = all_clean_data['acl']
    #     photo = all_clean_data['photo']
    #     details = all_clean_data['details']
