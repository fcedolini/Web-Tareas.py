from django.apps import AppConfig


# nombre de clase principal de la app q debe ser incluida en el "settings.py" INSTALLED_APPS
class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
