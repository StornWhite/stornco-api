from stornco.libs.tests.basetestcases import BaseAPITestCase
from ...models import Hello
from ..factories import HelloFactory


class HelloAPITestCase(BaseAPITestCase):
    """
    Tests the Hello model endpoints.
    """
    base_url = '/api/v1/hello/'
    base_queryset = Hello.objects.all()

    def setUp(self):
        """
        Create the hello table.
        :return:
        """
        super().setUp()
        for i in range(0, 5):
            HelloFactory()

    def test_anonymous_forbidden(self):
        """
        Test that anonymous users get 403 responses for all methods at
        all regular object and list endpoints.
        """
        hello = Hello.objects.first()
        data = {}
        list_url = self.base_url
        obj_url = '%s%i/' % (list_url, hello.id)

        # Get
        response = self.client_anon.get(obj_url)
        self.assertEqual(response.status_code, 403)
        response = self.client_anon.get(list_url)
        self.assertEqual(response.status_code, 403)

        # Post
        response = self.client_anon.post(list_url, data)
        self.assertEqual(response.status_code, 403)

        # Put
        response = self.client_anon.put(obj_url, data)
        self.assertEqual(response.status_code, 403)

        # Patch
        response = self.client_anon.patch(obj_url, data)
        self.assertEqual(response.status_code, 403)
        response = self.client_anon.patch(list_url, data)
        self.assertEqual(response.status_code, 403)

        # Delete
        response = self.client_anon.delete(obj_url)
        self.assertEqual(response.status_code, 403)
        response = self.client_anon.delete(list_url)
        self.assertEqual(response.status_code, 403)

    def test_unauthorized_forbidden(self):
        """
        Test that unauthorized users get 403 responses for all methods at
        all regular object and list endpoints.
        """
        hello = Hello.objects.first()
        data = {}
        list_url = self.base_url
        obj_url = '%s%i/' % (list_url, hello.id)

        # Get
        response = self.client_unauth.get(obj_url)
        self.assertEqual(response.status_code, 403)
        response = self.client_unauth.get(list_url)
        self.assertEqual(response.status_code, 403)

        # Post
        response = self.client_unauth.post(list_url, data)
        self.assertEqual(response.status_code, 403)

        # Put
        response = self.client_unauth.put(obj_url, data)
        self.assertEqual(response.status_code, 403)

        # Patch
        response = self.client_unauth.patch(obj_url, data)
        self.assertEqual(response.status_code, 403)
        response = self.client_unauth.patch(list_url, data)
        self.assertEqual(response.status_code, 403)

        # Delete
        response = self.client_unauth.delete(obj_url)
        self.assertEqual(response.status_code, 403)
        response = self.client_unauth.delete(list_url)
        self.assertEqual(response.status_code, 403)

    def test_authorized_not_implemented(self):
        """
        Test that authorized users get 405 responses for all unimplemented
        methods at all regular object and list endpoints.
        """
        hello = Hello.objects.first()
        data = {}
        list_url = self.base_url
        obj_url = '%s%i/' % (list_url, hello.id)

        # Post
        response = self.client_auth.post(list_url, data)
        self.assertEqual(response.status_code, 405)

        # Put
        response = self.client_auth.put(obj_url, data)
        self.assertEqual(response.status_code, 405)

        # Patch
        response = self.client_auth.patch(obj_url, data)
        self.assertEqual(response.status_code, 405)
        response = self.client_auth.patch(list_url, data)
        self.assertEqual(response.status_code, 405)

        # Delete
        response = self.client_auth.delete(obj_url)
        self.assertEqual(response.status_code, 405)
        response = self.client_auth.delete(list_url)
        self.assertEqual(response.status_code, 405)

    def test_authorized_okay(self):
        """
        Test that authorized users successfully get data.
        """
        hello = Hello.objects.first()
        list_url = self.base_url
        obj_url = '%s%i/' % (list_url, hello.id)

        # Get object.
        response = self.client_auth.get(obj_url)
        self.assertEqual(response.status_code, 200)

        word = response.data.get('word')
        count = response.data.get('count')

        self.assertEqual(hello.word, word)
        self.assertEqual(hello.count, count)

        # Get list.
        response = self.client_auth.get(list_url)
        self.assertEqual(response.status_code, 200)

        word = response.data['results'][0]['word']
        count = response.data['results'][0]['count']

        self.assertEqual(hello.word, word)
        self.assertEqual(hello.count, count)

    def test_anonymous_echo(self):
        """
        Test that 
        """