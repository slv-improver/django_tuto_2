from django.shortcuts import render
from . import forms

def login_page(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = forms.LoginForm()
    return render(
        request,
        'authentication/login.html',
        {'form': form}
    )
