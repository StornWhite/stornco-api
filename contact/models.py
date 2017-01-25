from django.db import models


class ContactStornco(models.Model):
    """
    A message from a visitor reaching out to storn.co.
    """
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    body = models.TextField()
    cc_sender = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s - %s" % (self.email, self.subject)
