from django import forms
from .models import *
# Не надо так импортить. Во первых не понятно что используется в файле, во вторых
# в больших проектах могут возникнуть проблемы с рекурсивным импортом.
# импортить надо только то, что нужно


class PersonForm(forms.ModelForm):
    # имена переменных должны быть маленькими буквами. Большие допускаются только для классов
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя','class':'form-control',
                                                         'maxlength':'30'}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ваш email','class':'form-control'}))
    class Meta:
        model = Person
        exclude = [""] # ?

class Test(forms.Form):
    test_name = forms.CharField()
