from copy import deepcopy

from factory.fuzzy import FuzzyText

from stornco.libs.api import tests as api_tests
from ...models import Hello
from ..factories import HelloFactory


class HelloAPITestCase(
    api_tests.BaseAPITestCase,
    api_tests.AuthorizedOkayGetMixin,
    api_tests.AuthorizedNotImplementedMixin,
    api_tests.AnonymousNoAccessMixin,
    api_tests.UnauthorizedForbiddenTestCase
):
    """
    Tests the Hello model endpoints.
    """
    base_url = '/api/v1/hello/'
    base_queryset = Hello.objects.all()
    unimplemented_methods = ['post', 'put', 'patch', 'delete']

    def setUp(self):
        """
        Create the hello table.
        :return:
        """
        for i in range(0, 5):
            HelloFactory()

        super().setUp()

    def test_anonymous_echo(self):
        """
        Test that echo endpoint echos parameter
        """
        hello = Hello.objects.first()

        word = deepcopy(hello.word)
        count = deepcopy(hello.count)
        echo_url = self.base_url + 'echo/?hello=%s' % word

        response = self.client_anon.get(echo_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('word'), word)
        self.assertEqual(response.data.get('count'), count + 1)

    def test_url_encoding(self):
        """
        Test that encoded charector work.
        """
        word = "World's biggest Hello World."
        Hello.get_or_create(word=word)

        echo_url = self.base_url + 'echo/?hello=%s' % word

        response = self.client_anon.get(echo_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get('word'), word)
        self.assertEqual(response.data.get('count'), 1)

    def test_echo_nothing(self):
        """
        Test echo with no hello parameter.
        """
        echo_url = self.base_url + 'echo/'

        response = self.client_anon.get(echo_url)
        self.assertEqual(response.status_code, 400)

        echo_url = self.base_url + 'echo/?hello='

        response = self.client_anon.get(echo_url)
        self.assertEqual(response.status_code, 400)

        echo_url = self.base_url + 'echo/?my-butt=hello'

        response = self.client_anon.get(echo_url)
        self.assertEqual(response.status_code, 400)

    def test_echo_hello_too_long(self):
        """
        Test echo with parameter too long.
        """
        word = FuzzyText(length=50).fuzz()
        echo_url = self.base_url + 'echo/?hello=%s' % word

        response = self.client_anon.get(echo_url)
        self.assertEqual(response.status_code, 200)

        word = FuzzyText(length=51).fuzz()
        echo_url = self.base_url + 'echo/?hello=%s' % word

        response = self.client_anon.get(echo_url)
        self.assertEqual(response.status_code, 400)
