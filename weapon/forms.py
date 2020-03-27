from django import forms
from .models import User
from django.core.exceptions import *
import re

USERNAME_PATTERN = re.compile(r'\w{4,20}')


class UserForm(forms.ModelForm):
    def clean_username(self):
        username = self.cleaned_data['username']
        if not USERNAME_PATTERN.fullmatch(username):
            raise ValidationError('用户名由字母、数字和下划线构成且长度为4-20个字符')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8 or len(password) > 20:
            raise ValidationError('无效的密码，密码长度为8-20个字符')
        return password

    class Meta:
        model = User
