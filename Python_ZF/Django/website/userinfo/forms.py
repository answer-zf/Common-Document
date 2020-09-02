from django import forms


class RegForm(forms.Form):
    username = forms.CharField(label='pl. input name')
    password = forms.CharField(label='pl. input password')
