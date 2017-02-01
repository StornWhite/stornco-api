from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Hello


class HelloView(APIView):
    """
    API endpoint that accepts anonymous GET requests and echos the value
    of the reply parameter.
    """
    permission_classes = [AllowAny, ]

    # Todo - change this structure to build on top of standard APIModelView
    def get(self, request, pk=None, format=None):
        """
        Echo the value of the request's hello parameter and return a
        count of the number of times that word has been echoed in the past.

        e.g. api.storn.co/hello/?hello=goodbye returns:
        {"hello": "goodbye", "count": <count>}
        """
        hello_txt = request.GET.get('hello')

        if hello_txt:
            # Look for past hello
            try:
                hello = Hello.objects.get(word=hello_txt)
            except Hello.DoesNotExist:
                hello = Hello(word=hello_txt, count=0)

        reply = {
            'hello': hello.word,
            'count': hello.count()
        }

        return Response(reply)
