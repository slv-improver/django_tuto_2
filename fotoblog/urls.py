"""fotoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import authentication.views
import blog.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", authentication.views.login_page, name="login"),
    path("signup/", authentication.views.signup_page, name="signup"),
    path("logout/", authentication.views.logout_user, name="logout"),
    path("change-password/", authentication.views.change_password, name="change_password"),
    path("password-changed/", authentication.views.password_changed, name="password_changed"),
    path("profile/photo/", authentication.views.upload_profile_photo, name='profile_photo'),
    path("home/", blog.views.home, name="home"),
    path("blog/create/", blog.views.blog_and_photo_upload, name='create_post'),
    path("blog/<int:blog_id>", blog.views.blog_post, name='blog_post'),
    path("blog/<int:blog_id>/edit", blog.views.edit_post, name='edit_post'),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
