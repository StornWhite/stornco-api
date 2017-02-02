from django.db import models


class Hello(models.Model):
    """
    A word that has been echoed through the hello program and the number
    of times that it has been echoed.
    """
    word = models.CharField(
        max_length=50, db_index=True, unique=True
    )
    count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Hello'
        verbose_name_plural = 'Hellos'

    def __str__(self):
        return "%s: %i" % (self.word, self.count)

    @classmethod
    def get_or_create(cls, word):
        """
        If returns a matching Hello object if one can be found.  Otherwise,
        creates and returns a new object.

        :param word: string
        :return: Hello object
        """
        try:
            hello = cls.objects.get(word=word)
        except Hello.DoesNotExist:
            hello = cls(word=word, count=0)

        return hello
