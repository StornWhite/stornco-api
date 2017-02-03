from rest_framework import serializers

from .models import Hello


class HelloSerializer(serializers.HyperlinkedModelSerializer):
    """
    API serializer for the ContactStornco model.
    """

    class Meta:
        model = Hello
        fields = (
            'id',
            'word',
            'count'
        )