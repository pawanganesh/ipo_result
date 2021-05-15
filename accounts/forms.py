from django import forms
from django.contrib.auth import get_user_model


class LoginModelForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # class Meta:
    #     model = get_user_model()
    #     fields = ['username', 'password', ]
