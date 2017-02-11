from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Roof
from .serializers import RoofSerializer


class RoofModelViewSet(ModelViewSet):
    """
    API endpoint for creating, viewing, editing, and deleting Roof objects.
    """
    queryset = Roof.objects.all()
    serializer_class = RoofSerializer
    permission_classes = [IsAuthenticated, ]
