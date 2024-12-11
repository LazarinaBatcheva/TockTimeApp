"""
Custom manager for the AppUser model.

This module defines methods for creating users and superusers,
customizing the user creation process in Django.
"""

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class AppUserManager(BaseUserManager):
    """
    Custom manager for the AppUser model.

    This manager provides methods for creating users and superusers,
    ensuring proper validation and defaults during the creation process.
    """

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Internal method to create and save a user with the given username, email, and password.
        """

        if not username:
            raise ValueError("The given username must be set")

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        """ Create and save a regular user with the given username, email, and password. """

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """ Create and save a superuser with the given username, email, and password. """

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

