from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d\'utilisateur')
    password = form.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
