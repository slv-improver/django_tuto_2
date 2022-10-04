from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from . import forms
from . import models

@login_required
def home(r):
    photos = models.Photo.objects.all()
    return render(r, 'blog/home.html', {'photos': photos})

@login_required
def blog_and_photo_upload(req):
    if req.method == 'POST':
        blog_form = forms.BlogForm(req.POST)
        photo_form = forms.PhotoForm(req.POST, req.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = req.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = req.user
            blog.photo = photo
            blog.save()
            return redirect('home')
    else:
        blog_form = forms.BlogForm()
        photo_form = forms.PhotoForm()
    return render(
        req,
        'blog/create_blog_post.html',
        {'blog_form': blog_form, 'photo_form': photo_form}
    )

def blog_post(req, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(
        req,
        'blog/blog_post.html',
        {'blog': blog}
    )
