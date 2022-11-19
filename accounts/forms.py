from django import forms

from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    username = forms.CharField( widget = forms.Textarea , required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget = forms.PasswordInput , required = True)
