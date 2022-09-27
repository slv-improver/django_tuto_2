from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(r):
    return render(r, 'blog/home.html')
