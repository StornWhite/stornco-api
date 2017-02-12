from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Roof
from .serializers import RoofSerializer


class RoofModelViewSet(ModelViewSet):
    """
    API endpoint for creating, viewing, editing, and deleting Roof objects.
    """
    queryset = Roof.objects.all().order_by('id')
    serializer_class = RoofSerializer
    # Todo: change to IsAuthenticated
    permission_classes = [AllowAny, ]
