"""
Signal handlers for the accounts app.

This module defines signals to automatically manage the relationship
between the UserModel and the Profile model.
"""

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from tock_time_app.accounts.models import Profile

# Get the custom user model
UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a Profile when a UserModel instance is created.
    Args:
        sender: The model class that triggered the signal (UserModel).
        instance: The instance of the sender (a user object).
        created (bool): True if a new instance was created.
        **kwargs: Additional keyword arguments.
    """

    if created:     # Only create a profile if the user instance is newly created
        Profile.objects.create(user=instance)   # Create a Profile linked to the user


@receiver(post_delete, sender=Profile)
def delete_user_on_profile_delete(sender, instance,  **kwargs):
    """
    Signal handler to delete a UserModel instance when its Profile is deleted.
    Args:
        sender: The model class that triggered the signal (Profile).
        instance: The instance of the sender (a profile object).
        **kwargs: Additional keyword arguments.
    """

    if instance.user:   # Ensure the profile is linked to a user
        instance.user.delete()  # Delete the linked user instance
