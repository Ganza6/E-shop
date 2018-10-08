from django import forms
from .models import *

class PersonForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя','class':'form-control',
                                                         'maxlength':'30'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ваш email','class':'form-control'}))
    class Meta:
        model = Person
        exclude = [""]

class Test(forms.Form):
    test_name = forms.CharField()