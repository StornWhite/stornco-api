from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import list_route

from .models import Hello
from .serializers import HelloSerializer


class HelloModelViewSet(ReadOnlyModelViewSet):
    """
    API endpoint that accepts anonymous GET requests and echos the value
    of the reply parameter.
    """
    queryset = Hello.objects.all()
    serializer_class = HelloSerializer
    permission_classes = [IsAuthenticated, ]
    http_method_names = ['get', ]

    @list_route(methods=['get'], permission_classes=[AllowAny])
    def echo(self, request, pk=None, format=None):
        """
        Echos the message and a count of all previous echos to the message.

        Message is delivered as a url parameter named hello, as in:
        api.storn.co/api/v1/hello/echo?hello=hello-world

        Responds with json payload {"hello": "hello-world", "count": count}
        """
        hello_txt = request.GET.get('hello')

        if hello_txt:
            hello = Hello.get_or_create(hello_txt)
            hello.count += 1
            hello.save()
            reply = HelloSerializer(hello).data
            return Response(reply)
        else:
            raise ValidationError("You didn't say hello!")
