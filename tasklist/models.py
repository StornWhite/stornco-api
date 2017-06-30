from django.db import models
from django.db import transaction
from django.core.validators import MinValueValidator

from stornco.libs.models import TimeStampMixin
from authorize.models import User


class Task(TimeStampMixin, models.Model):
    """
    Represents an a task to be completed.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(limit_value=1)
        ]
    )
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['priority']
        unique_together = ('priority', 'user')

    @property
    def user_tasks(self):
        """
        Returns all tasks related to the task's user.

        :return: queryset of Task objects
        """
        return Task.objects.filter(user=self.user)

    @property
    def incomplete_user_tasks(self):
        """
        Returns all incomplete tasks related to the task's user.

        :return: queryset of Task objects
        """
        return self.user_tasks.filter(is_complete=False)

    @classmethod
    def get_next_priority(cls, user):
        """
        Return the lowest unused priority.

        :return: integer next priority
        """
        tasks = cls.objects.filter(user=user, is_complete=False)
        last = tasks.last()
        if last:
            return last.priority + 1
        else:
            return 1

    @classmethod
    @transaction.atomic()
    def create_priority_gap(cls, user, priority, task_id=None):
        """
        If task priority will duplicate the priority of another incomplete
        task, rejigger the other incomplete tasks' priorities to make room.
        """
        tasks = cls.objects.filter(user=user)
        if task_id:
            tasks = tasks.exclude(pk=task_id)

        # Look for duplicate priority.
        if tasks.filter(priority=priority).count() > 0:
            to_rejigger = tasks.filter(
                priority__gte=priority
            ).order_by('-priority')
            for task in to_rejigger:
                task.priority += 1
                task.save()

    @ classmethod
    @transaction.atomic()
    def fill_priority_gaps(cls, user):
        """
        Closes the gaps in the priority ranking of a user's tasks.
        """
        print('hi im in the fill thing')
        tasks = cls.objects.filter(user=user, is_complete=False)
        i = 0
        print('hi I found {} tasks'.format(tasks.count()))
        for task in tasks:
            i += 1
            if task.priority != i:
                print('hey task id={} has priority {} instead of {}'.format(task.id, task.priority, i))
                task.priority = i
                task.save()
                print('hey i just saved a task')

    def delete(self, *args, **kwargs):
        """
        Fill the gap in priority left behind by deleting a task.
        """
        user = None
        if self.priority:
            # We'll need to fill gaps if deleted task has a priority.
            user = self.user

        super().delete(*args, **kwargs)

        if user:
            Task.fill_priority_gaps(user)
