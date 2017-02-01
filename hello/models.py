from django.db import models


class Hello(models.Model):
    """
    A word that has been echoed through the hello program and the number
    of times that it has been echoed.
    """
    word = models.CharField(
        max_length=50, db_index=True, unique=True
    )
    count = models.IntegerField()

    class Meta:
        verbose_name = 'Hello'
        verbose_name_plural = 'Hellos'

    def __str__(self):
        return "%s: %i" % (self.word, self.count)
