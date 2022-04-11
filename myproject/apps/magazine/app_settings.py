# myproject/apps/magazine/app_settings.py
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Example:
ARTICLE_THEME_CHOICES = getattr(
   settings,
   "MAGAZINE_ARTICLE_THEME_CHOICES",
   [
       ('futurism', _("Futurism")),
       ('nostalgia', _("Nostalgia")),
       ('sustainability', _("Sustainability")),
       ('wonder', _("Wonder")),
] )
