from django import forms
import re

mobile_re = re.compile(
    r'^(13[0-9]|15[0123456789]|17[678]|18[0-9]|14[57])[0-9]{8}$')


def mobile_validate(value):
    if not mobile_re.match(value):
        raise forms.ValidationError('手机号码各式错误')


class RegForm(forms.Form):
    username = forms.CharField(label='pl. input name')
    password = forms.CharField(
        label='pl. input password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='pl. input password2', widget=forms.PasswordInput)
    mobile = forms.CharField(label='mobile phont',
                             validators=[mobile_validate])

    def clean(self):
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError('PASSWORD INCONSISTENCY!!!')
        print(self.cleaned_data)
        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data["username"]
        if len(username) < 6:
            raise forms.ValidationError('username to short')

        return username
