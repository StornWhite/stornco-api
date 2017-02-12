from rest_framework.serializers import HyperlinkedModelSerializer, DecimalField

from .models import Roof


class RoofSerializer(HyperlinkedModelSerializer):
    """
    API serializer for the Roof model.
    """
    # Needed to coerce to string.
    area = DecimalField(
        required=False,
        max_digits=14,
        decimal_places=2,
        coerce_to_string=True
    )

    class Meta:
        model = Roof
        fields = (
            'id',
            'name',
            'shape',
            'base',
            'height',
            'area',
            'pitch',
            'aspect',
            'longitude',
            'latitude'
        )
