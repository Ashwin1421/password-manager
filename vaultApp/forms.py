from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import PasswordEntry


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


class PasswordEntryForm(forms.Form):
    website = forms.CharField(max_length=150, required=True)
    username = forms.CharField(max_length=150, required=True)
    plaintext_password = forms.CharField(max_length=128, required=True, widget=forms.PasswordInput)

    class Meta:
        model = PasswordEntry
        fields = ('username', 'plaintext_password', 'website', 'date_of_creation')


class RandomPasswordGenerationForm(forms.Form):
    random_plaintext_password = forms.CharField(
        max_length=150,
        required=True,
        help_text="Required",
        label="Generate new random password"
    )

    class Meta:
        model = PasswordEntry
        fields = ('random_plaintext_password',)
