import unittest

from rest_framework.test import APITestCase, APIClient
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authentication import SessionAuthentication
from rest_framework.settings import api_settings

from authorize.tests.factories import UserFactory


class BaseAPITestCase(APITestCase):
    """
    A base test case that defines authorized, unauthorized, and
    staff users during setup and then tests all unimplemented and unauthorized
    cases.
    """
    def setUp(self):
        # Factory creates mock users with password = pa55word.
        self.user_auth = UserFactory()
        self.user_unauth = UserFactory(is_active=False)
        self.user_staff = UserFactory(is_staff=True)

        # Create clients.
        self.client_anon = APIClient()

        self.client_auth = APIClient()
        self.client_auth.login(
            email=self.user_auth.email,
            password='pa55word'
        )

        self.client_unauth = APIClient()
        self.client_unauth.login(
            email=self.user_unauth.email,
            password='pa55word'
        )

        self.client_staff = APIClient()
        self.client_staff.login(
            email=self.user_staff.email,
            password='pa55word'
        )
