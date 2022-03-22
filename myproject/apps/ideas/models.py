# myproject/apps/ideas/models.py
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from myproject.apps.core.models import UrlBase, CreationModificationDateBase


class Idea(UrlBase, CreationModificationDateBase):
    # fields, attributes, properties and methods...

    def get_url_path(self):
        return reverse("idea_details", kwargs={
            "idea_id": str(self.pk),
        })
