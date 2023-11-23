from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your_Name', 'class': 'w-full px-6 py-4 rounded-xl outline-none'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Your_Name', 'class': 'w-full px-6 py-4 rounded-xl outline-none'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'w-full px-6 py-4 rounded-xl outline-none'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re_entered_password', 'class': 'mb-6 w-full px-6 py-4 rounded-xl outline-none'}))
