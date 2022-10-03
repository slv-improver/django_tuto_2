from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

@login_required
def home(r):
    return render(r, 'blog/home.html')

@login_required
def photo_upload(req):
    if req.method == 'POST':
        form = forms.PhotoForm(req.POST, req.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = req.user
            photo.save()
            return redirect('home')
    else:
        form = forms.PhotoForm()
    return render(
        req,
        'blog/photo_upload.html',
        {'form': form}
    )
