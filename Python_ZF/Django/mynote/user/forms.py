from django import forms
import re


class RegForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.clean_username['username']
        if len(username) < 6:
            raise forms.ValidationError('username to short')

        return username

    def clean_password(self):
        password = self.clean_password['password']

        password_re = re.compile(r'[A-Za-z\d]{6,10}')
        if not password_re.match(password):
            raise forms.ValidationError('password mistake')

        return password

    def clean(self):
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']
        if pwd2 != pwd1:
            raise forms.ValidationError('password mistake')
        return self.cleaned_data
