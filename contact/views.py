from rest_framework import viewsets

from .models import ContactStornco
from .serializers import ContactStorncoSerializer


class ContactStorncoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows anonymous users to contact stornco and
    that allows stornco staff to retrieve and view past contacts.
    """
    queryset = ContactStornco.objects.all().order_by('created_at')
    serializer_class = ContactStorncoSerializer
    # Todo: limit this to POST for anonymous users.
    # Todo: throttle this
    # Todo: limit to view list and object for authorized users.