from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    class Meta:
        abstract = True

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        default=None,
        null=True,
        related_name="+",
        on_delete=models.PROTECT,
    )
