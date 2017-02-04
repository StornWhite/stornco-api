# Factories for creating User and other authorize model objects for testing.

import factory
from ..models import User


class UserFactory(factory.DjangoModelFactory):
    """
    Creates a mock user object with password = 'pa55word.'
    """
    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'email-%d@example.com' % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    password = factory.PostGenerationMethodCall('set_password', 'pa55word')
    is_active = True
    is_staff = False
