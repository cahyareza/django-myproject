from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class IdeasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "myproject.apps.ideas"
    verbose_name = _("Ideas")
