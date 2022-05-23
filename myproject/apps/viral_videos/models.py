import re
from django.db import models
from django.utils.translation import ugettext_lazy as _

from myproject.apps.core.models import CreationModificationDateBase, UrlBase


class ViralVideo(CreationModificationDateBase, UrlBase):
    title = models.CharField(
        _("Title"),
        max_length=200,
        blank=True)
    embed_code = models.TextField(
        _("YouTube embed code"),
        blank=True)
    anonymous_views = models.PositiveIntegerField(
        _("Anonymous impressions"),
        default=0)
    authenticated_views = models.PositiveIntegerField(
        _("Authenticated impressions"),
        default=0)

    class Meta:
        verbose_name = _("Viral video")
        verbose_name_plural = _("Viral videos")

    def __str__(self):
        return self.title

    def get_url_path(self):
        from django.urls import reverse
        return reverse("viral-video-detail",
                       kwargs={"pk": str(self.pk)})