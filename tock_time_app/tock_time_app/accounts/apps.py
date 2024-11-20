from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tock_time_app.accounts'

    def ready(self):
        import tock_time_app.accounts.signals
