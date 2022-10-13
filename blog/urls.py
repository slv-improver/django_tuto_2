from django.urls import path
from django.conf import settings
import blog.views

urlpatterns = [
    path("create/", blog.views.blog_and_photo_upload, name='create_post'),
    path("<int:blog_id>/", blog.views.blog_post, name='blog_post'),
    path("<int:blog_id>/edit/", blog.views.edit_post, name='edit_post'),
]
