from django import forms
import re


class RegForm(forms.Form):

    def clean(self):
        pwd1 = self.data.get('password')
        pwd2 = self.data.get('password2')
        print(self.cleaned_data)
        if pwd2 != pwd1:
            raise forms.ValidationError('password mistake')
        return self.cleaned_data

    def clean_username(self):
        username = self.data.get('username')
        if len(username) < 6:
            raise forms.ValidationError('username to short')

        return username

    def clean_password(self):
        password = self.data.get('password')

        password_re = re.compile(r'[A-Za-z\d]{6,10}')
        if not password_re.match(password):
            raise forms.ValidationError('password mistake')

        return password


class LoginForm(forms.Form):

    def clean(self):
        # username = self.clean_username['username']
        print(self.data)
        return self.cleaned_data

    def clean_username(self):
        username = self.data.get('username')
        print(username)
        if len(username) < 6:
            raise forms.ValidationError('username to short')

        return username

    def clean_password(self):
        password = self.data.get('password')

        password_re = re.compile(r'[A-Za-z\d]{6,10}')
        if not password_re.match(password):
            raise forms.ValidationError('password mistake')

        return password
