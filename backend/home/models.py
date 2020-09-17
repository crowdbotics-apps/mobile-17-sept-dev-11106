from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    ghfhfh = models.CharField(
        max_length=150,
        blank=True,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"


class Gffjhgf(models.Model):
    "Generated Model"
    jhgfjhg = models.BigIntegerField()
    fhgfhgf = models.ForeignKey(
        "home.CustomText",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="gffjhgf_fhgfhgf",
    )
