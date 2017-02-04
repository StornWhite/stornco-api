# Factories for creating hello model objects for testing.

from factory import DjangoModelFactory
from factory.fuzzy import FuzzyText, FuzzyInteger

from ..models import Hello


class HelloFactory(DjangoModelFactory):
    """
    Creates a mock Hello object.
    """
    class Meta:
        model = Hello

    word = FuzzyText()
    count = FuzzyInteger(low=0, high=1000000)
