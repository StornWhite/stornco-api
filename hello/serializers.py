from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Hello


class HelloSerializer(serializers.HyperlinkedModelSerializer):
    """
    API serializer for the ContactStornco model.
    """
    def __init__(self, *args, **kwargs):
        """
        Remove the UniqueValidator from the word field so we won't error
        on field matching before get_or_create.
        """
        super().__init__(*args, **kwargs)

        word_field = self.fields['word']
        new_validators = [validator for validator in word_field.validators
                          if not isinstance(validator, UniqueValidator)]
        word_field.validators = new_validators

    class Meta:
        model = Hello
        fields = (
            'id',
            'word',
            'count'
        )
