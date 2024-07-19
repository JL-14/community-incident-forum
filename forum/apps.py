"""Imports and configures the Forum app."""
from django.apps import AppConfig


class ForumConfig(AppConfig):
    """Sets Django for the forum app."""
    
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forum'
