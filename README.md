# FOTOBLOG project

OpenClassrooms course

## App configuration

To create a personnalized User model, extend the User class from AbstractUser (or AbstractBaseUser to get an empty User model)

Add `BASE_DIR.joinpath('templates')` in settings.py TEMPLATES DIRS to use base.html on all apps

To create user in django shell:</br>
- `from authentication.models import User`
- `User.objects.create_user(username='algor', password='S3cret!', role='CREATOR')`

To add permissions to Users, in django shell:</br>
- `from authentication.models import User`
- `from django.contrib.auth.models import Permission`
- `user = User.objects.get(username='algor')`
- `permission = Permission.objects.get(codename='add_blog')`
- `user.user_permissions.add(permission)`