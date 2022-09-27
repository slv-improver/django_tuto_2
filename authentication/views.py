from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from . import forms

def logout_user(request):
    logout(request)
    return redirect('login')

def login_page(request):
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Hi, {user.username}! You\'re logged in.'
            else:
                message = 'Invalid credentials .'
    else:
        form = forms.LoginForm()
    return render(
        request,
        'authentication/login.html',
        {'form': form, 'message': message}
    )
