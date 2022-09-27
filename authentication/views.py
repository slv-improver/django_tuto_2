from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms

def logout_user(r):
    logout(r)
    return redirect('login')


class LoginPageView(View):
    template_name = 'authentication/login.html'
    form_class = forms.LoginForm

    def get(self, r):
        form = self.form_class()
        message = ''
        return render(
            r,
            self.template_name,
            {'form': form, 'message': message}
        )
    
    def post(self, r):
        form = self.form_class(r.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(r, user)
                return redirect('home')
        message = 'Invalid credentials .'
        return render(
            r,
            'authentication/login.html',
            {'form': form, 'message': message}
        )
