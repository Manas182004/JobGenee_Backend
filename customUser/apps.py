from django.apps import AppConfig

class CustomUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customUser'  # Ensure this matches your app's folder name
