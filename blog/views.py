from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from . import forms
from . import models

@login_required
@permission_required('blog.view_blog', raise_exception=True)
def home(r):
    blogs = models.Blog.objects.filter(
        Q(contributors__in=r.user.follows.all()) | Q(starred=True)
    ).order_by('-date_created')
    # photos = models.Photo.objects.filter(
    #     uploader__in=r.user.follows.all()
    # ).exclude(
    #     blog__in=blogs
    # )
    return render(r, 'blog/home.html', {
        'blogs': blogs,
        # 'photos': photos
    })

@login_required
@permission_required('blog.add_blog', raise_exception=True)
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
            blog.contributors.add(
                req.user,
                through_defaults={'contribution': 'Main author'}
            )
            return redirect('home')
    else:
        blog_form = forms.BlogForm()
        photo_form = forms.PhotoForm()
    return render(
        req,
        'blog/create_blog_post.html',
        {'blog_form': blog_form, 'photo_form': photo_form}
    )

@login_required
@permission_required('blog.view_blog', raise_exception=True)
def blog_post(req, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(
        req,
        'blog/blog_post.html',
        {'blog': blog}
    )

@login_required
@permission_required(['blog.change_blog'], raise_exception=True)
def edit_post(req, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    photo = blog.photo
    if req.method == 'POST':
        if 'edit_blog' in req.POST:
            print(req.POST)
            edit_blog_form = forms.BlogForm(req.POST, instance=blog)
            edit_photo_form = forms.PhotoForm(req.POST, req.FILES, instance=photo)
            if all([edit_blog_form.is_valid(), edit_photo_form.is_valid()]):
                photo = edit_photo_form.save(commit=False)
                photo.uploader = req.user
                photo.save()
                blog = edit_blog_form.save(commit=False)
                blog.contributors.add(
                    req.user,
                    through_defaults={'contribution': 'contributor'}
                )
                blog.photo = photo
                blog.save()
                return redirect('blog_post', blog_id=blog_id)
        elif 'delete_blog' in req.POST:
            delete_form = forms.DeleteBlogForm(req.POST)
            if delete_form.is_valid():
                blog.delete()
                return redirect('home')
    else:
        edit_blog_form = forms.BlogForm(instance=blog)
        edit_photo_form = forms.PhotoForm(instance=photo)
        delete_form = forms.DeleteBlogForm()
    return render(
        req,
        'blog/edit_blog.html',
        {
            'edit_blog_form': edit_blog_form,
            'edit_photo_form': edit_photo_form,
            'delete_form': delete_form
        }
    )

@login_required
def follow_users(req):
    if req.method == 'POST':
        form = forms.FollowUsersForm(req.POST, instance=req.user)
        print(form.is_valid())
        print(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.FollowUsersForm()
    return render(
        req,
        'blog/follow_users_form.html',
        {'form': form}
    )
