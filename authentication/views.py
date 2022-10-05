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

def change_password(req):
    if req.method == 'POST':
        form = forms.UpdatePasswordForm(req.POST)
        if form.is_valid():
            user = authenticate(
                username=req.user.username,
                password=form.cleaned_data['old_password']
            )
            if user is not None:
                user.set_password(form.cleaned_data['new_password'])
                user.save()
                login(req, user)
                return redirect('password_changed')
    else:
        form = forms.UpdatePasswordForm()
    return render(
        req,
        'authentication/password_change_form.html',
        {'form': form}
    )

def password_changed(req):
    return render(
        req,
        'authentication/password_changed.html'
    )

def upload_profile_photo(req):
    if req.method == 'POST':
        form = forms.UploadProfilePhotoForm(req.POST, req.FILES, instance=req.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.UploadProfilePhotoForm(instance=req.user)
    return render(
        req,
        'authentication/upload_profile_photo.html',
        {'form': form}
    )
