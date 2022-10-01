from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import forms

def logout_user(req):
    logout(req)
    return redirect('login')

def login_page(req):
    message = ''
    if req.method == 'POST':
        form = forms.LoginForm(req.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(req, user)
                return redirect('home')
            else:
                message = 'Invalid credentials .'
    else:
        form = forms.LoginForm()
    return render(
        req,
        'authentication/login.html',
        {'form': form, 'message': message}
    )
