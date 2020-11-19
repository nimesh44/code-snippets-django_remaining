from django import forms


class UserLogin(forms.Form):
    username = forms.CharField()
    passowrd = forms.CharField(widget = forms.PasswordInput)