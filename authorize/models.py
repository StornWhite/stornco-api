from django.db import models
from django.contrib.auth.models import AbstractBaseUser

'''
class User(AbstractBaseUser):
    """
    User model is customized to require email addresses as identifier.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Required by AbstractBaseUser.
    def get_short_name(self):
        return self.first_name

    # Required by AbstractBaseUser.
    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
'''