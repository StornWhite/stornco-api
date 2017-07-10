from django.db import transaction

from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from .models import Task
from .exceptions import NewTaskMarkedCompleteError, ChangeUserError


class TaskSerializer(ModelSerializer):
    """
    API serializer for the Task model.
    """

    def __init__(self, *args, **kwargs):
        """
        Remove the UniqueTogetherValidator so that we can sort out duplicate
        priorities in the create or update methods.
        """
        super().__init__(*args, **kwargs)

        self.validators = [validator for validator in self.validators if not
                           isinstance(validator, UniqueTogetherValidator)]

    @transaction.atomic()
    def create(self, validated_data):
        """
        If priority is not assigned or too high, sets priority to lowest
        unused priority.  If priority conflicts with existing priority,
        rejiggers existing task priorities to make room.
        """
        if validated_data.get('is_complete'):
            exception = NewTaskMarkedCompleteError()
            exception.detail = {'is_complete': exception.default_detail}
            raise exception

        user = self.context['request'].user
        validated_data['user'] = user

        priority = validated_data.get('priority')
        next_priority = Task.get_next_priority(user)

        if priority:
            validated_data = self.update_priority(validated_data)
        else:
            # Apply lowest priority.
            validated_data['priority'] = next_priority

        task = Task(**validated_data)
        task.save()
        return task

    @transaction.atomic()
    def update(self, instance, validated_data):
        """
        If update marks task complete, remove priority and rejigger the
        remaining task priorities to fill the gap.  If update changes priority,
        rejigger the other tasks to make room.
        """
        # Raise error if attempting to change the User related to task.
        user = validated_data.get('user')
        if user and user != instance.user:
            raise ChangeUserError()

        # If task is transitioning to complete, remove priority.
        fill_gaps = False
        if 'is_complete' in validated_data:
            if validated_data['is_complete']:
                if not instance.is_complete:
                    # Task is transitioning to complete.
                    validated_data['priority'] = None
                    fill_gaps = True
            else:
                if instance.is_complete:
                    # Task is transitioning to incomplete.
                    validated_data = self.update_priority(validated_data)

        # If priority is changing, make sure new priority will be valid.
        priority = validated_data.get('priority')
        if priority and priority != instance.priority:
            validated_data = self.update_priority(validated_data)

        # Update instance.
        if 'name' in validated_data:
            instance.name = validated_data.get('name')
        if 'description' in validated_data:
            instance.description = validated_data.get('description')
        if 'priority' in validated_data:
            instance.priority = validated_data.get('priority')
        if 'is_complete' in validated_data:
            instance.is_complete = validated_data.get('is_complete')

        instance.save()

        if fill_gaps:
            user = self.context['request'].user
            Task.fill_priority_gaps(user)

        return instance

    def update_priority(self, validated_data):
        """
        If priority is not assigned or too high, sets priority in
        validated_data to lowest unused priority.  If priority conflicts with
        existing priority, rejiggers existing task priorities to make room.

        :return: dictionary validated_data with updated priority
        """
        user = self.context['request'].user
        priority = validated_data.get('priority')
        next_priority = Task.get_next_priority(user)

        if not priority or priority > next_priority:
            # Apply lowest priority
            validated_data['priority'] = next_priority
            return validated_data

        if priority < next_priority:
            # Create space between other tasks for this priority.
            Task.create_priority_gap(
                user=user,
                priority=priority
            )

        return validated_data

    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'description',
            'priority',
            'is_complete',
            'user',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
            'user',
            'created_at',
            'updated_at'
        )
