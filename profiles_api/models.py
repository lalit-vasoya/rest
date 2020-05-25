from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """ Model Manager for Profiles """

    def create_user(self,email,name,password=None):
        """ Create new user Profile """

        if not email:
            raise ValueError('User must have an email address');

        email = self.normalize_email(email)
        user  = self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """ Create new super user for system """

        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """ Database model for user profile """

    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELS = ['name']

    def get_full_name(self):
        """ Return full name of user """
        return self.name

    def get_short_name(self):
        """ Return short name of user """
        return self.name

    def __str__(self):
        """ Return string represtation of user """
        return self.email
