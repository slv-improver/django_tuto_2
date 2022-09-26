# FOTOBLOG project

OpenClassrooms course

## App configuration

To create a personnalized User model, extend the User class from AbstractUser (or AbstractBaseUser to get an empty User model)

Add `BASE_DIR.joinpath('templates')` in settings.py TEMPLATES DIRS to use base.html on all apps

To create user in django shell:</br>
- `from authentication.models import User`
- `User.objects.create_user(username='algor', password='S3cret!', role='CREATOR')`