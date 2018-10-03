from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2',)
