# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# Adds things to the user sign-up form
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'IDNumber', 'Node')

class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'IDNumber', 'Node',)
