# myproject/apps/categories/models.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    # fields, attributes, properties, and methods...
    def get_ideas_without_this_category(self):
        from myproject.apps.ideas.models import Idea
        return Idea.objects.exclude(category=self)