"""
App configuration for the accounts app.

This module defines the configuration settings for the accounts app,
including signal registration during app initialization.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tock_time_app.accounts'

    def ready(self):
        """
        Called when the app is ready.
        This method imports the signals module to register any signal handlers.
        """

        import tock_time_app.accounts.signals   # Ensure signals are connected when the app is loaded
