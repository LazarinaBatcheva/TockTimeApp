"""
Custom user model for the accounts app.
The AppUser model extends AbstractBaseUser and PermissionsMixin
to provide flexibility for authentication and user management.
"""

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from tock_time_app.accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    """ A custom user model with username, email, and account status fields. """

    class Meta:
        verbose_name = 'User account'
        verbose_name_plural = 'User accounts'

    username = models.CharField(
        max_length=100,
        unique=True,
    )

    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = AppUserManager()

    def __str__(self):
        return self.username
