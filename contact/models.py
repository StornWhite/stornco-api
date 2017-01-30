from django.db import models

from authorize.models import User


class ContactStornco(models.Model):
    """
    A message from a visitor reaching out to storn.co.
    """
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    body = models.TextField()
    cc_sender = models.BooleanField(default=True)
    owner = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Stornco Contact'
        verbose_name_plural = 'Stornco Contacts'

    def __str__(self):
        return "%s - %s" % (self.email, self.subject)
