from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models

@login_required
def home(r):
    photos = models.Photo.objects.all()
    return render(r, 'blog/home.html', {'photos': photos})

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

def change_photo(req):
    pass
