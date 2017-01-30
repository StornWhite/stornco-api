from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import ContactStornco
from .serializers import ContactStorncoSerializer


class ContactStorncoViewSet(ModelViewSet):
    """
    API endpoint that allows anonymous users to contact stornco and
    that allows stornco staff to retrieve and view past contacts.
    """
    queryset = ContactStornco.objects.all().order_by('created_at')
    serializer_class = ContactStorncoSerializer
    http_method_names = ['get', 'post', 'head']
    permission_classes = [IsAuthenticated, ]

    def get_permissions(self):
        """
        Adjust permissions to allow anonymous users to POST.
        """
        if self.request.method == 'POST':
            permissions = [AllowAny, ]
        else:
            permissions = self.permission_classes
        return [permission() for permission in permissions]

    def get_queryset(self):
        """
        For staff users, returns all contact messages.  For authenticated
        non-staff users, returns their own contact messages only.

        :return: QuerySet of ContactStornco objects
        """
        if self.request.user.is_staff:
            return ContactStornco.objects.all()
        else:
            return ContactStornco.objects.filter(
                owner=self.request.user
            )
