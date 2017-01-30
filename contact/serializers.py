from rest_framework import serializers

from .models import ContactStornco


class ContactStorncoSerializer(serializers.HyperlinkedModelSerializer):
    """
    API serializer for the ContactStornco model.
    """

    class Meta:
        model = ContactStornco
        fields = (
            'id',
            'email',
            'subject',
            'body',
            'cc_sender',
            'owner',
            'created_at'
        )
