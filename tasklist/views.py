from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Task
from .serializers import TaskSerializer


class TaskModelViewSet(ModelViewSet):
    """
    API endpoint for creating, viewing, editing, and deleting Task objects.
    """
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        """
        Users may see their own tasks only.
        """
        return Task.objects.filter(user=self.request.user)
