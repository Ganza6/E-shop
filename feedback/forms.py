from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя','class': 'form-control',
                                                         'maxlength': '30'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ваш email','class': 'form-control'}))

    class Meta:
        model = Person
        exclude = [""]
