"""
Profile model for extending user functionality.
The Profile model is linked to the AppUser model and adds fields for first name, last name, and profile picture.
"""

from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    """ A model representing additional user profile details. """

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    friends = models.ManyToManyField(
        to='self',
        symmetrical=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = CloudinaryField(
        null=True,
        blank=True,
    )

    def get_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.user.username

    def __str__(self):
        return self.get_name()
