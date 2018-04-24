from django import forms

from django.contrib.auth.models import User


class UserSignupFrom(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Password Confirm', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'password_confirm', )
