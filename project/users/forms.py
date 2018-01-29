from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    username = forms.CharField(max_length=50, required=True)
    full_name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'full_name', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

