from cloudinary.models import CloudinaryField
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to='accounts.AppUser',
        on_delete=models.CASCADE,
        related_name='profile',
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

        return self.first_name or self.last_name or self.user.username

    def __str__(self):
        return self.get_name()
