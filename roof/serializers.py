from rest_framework.serializers import ModelSerializer

from .models import Roof


class RoofSerializer(ModelSerializer):
    """
    API serializer for the Roof model.
    """
    class Meta:
        model = Roof
        fields = (
            'id',
            'name',
            'shape',
            'base',
            'height',
            'pitch',
            'aspect',
            'longitude',
            'latitude'
        )
