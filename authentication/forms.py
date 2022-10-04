from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from . import models

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Username')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Password')

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'role')

class UpdatePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Old password')
    new_password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='New password')
    new_password_confirmation = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Confirmation')

class UploadProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('profile_photo',)
