from django.db import models


class TimeStampMixin(models.Model):
    """
    Adds automatically generated created_at and updated_at fields to
    models.
    """
    created_at = models.DateTimeField(
        verbose_name='Created',
        auto_now=False,
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated',
        auto_now=True
    )

    class Meta:
        abstract = True
