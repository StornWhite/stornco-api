from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class HelloView(APIView):
    """
    API endpoint that accepts anonymous GET requests and echos the value
    of the reply parameter.
    """
    permission_classes = [AllowAny, ]

    def get(self, request, pk=None, format=None):
        """
        Echo the value of the request's echo parameter.

        e.g. api.storn.co/hello/?echo=goodbye returns {"echo": "goodbye"}
        """
        echo = request.GET.get('echo')
        reply = {'echo': echo if echo else 'Hello'}

        return Response(reply)
