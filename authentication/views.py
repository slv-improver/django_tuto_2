from django.conf import settings
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import forms

def logout_user(req):
    logout(req)
    return redirect('login')

def signup_page(req):
    if req.method == 'POST':
        form = forms.SignupForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = forms.SignupForm()
    return render(
        req,
        'authentication/signup.html',
        {'form': form}
    )

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

def change_password(req, loggedin_user):
    if req.method == 'POST':
        form = forms.UpdatePasswordForm(req.POST)
        if form.is_valid():
            user = authenticate(
                username=loggedin_user.username,
                password=form.cleaned_data['old_password']
            )
            if user is not None:
                user.password = form.new_password
                user.save()
                password_changed()
    else:
        form = forms.UpdatePasswordForm()
    return render(
        req,
        'authentication/password_change_form.html',
        {'form': form}
    )

def password_changed(req):
    pass
