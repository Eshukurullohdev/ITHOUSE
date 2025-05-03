from django.apps import AppConfig


class HouseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'House'


class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'House'

    def ready(self):
        import House.signals  # Import the receiver module here to ensure it's loaded when the app is ready
