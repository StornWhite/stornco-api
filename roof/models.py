from django.db import models


class Roof(models.Model):
    """
    Represents a planar roof surface.
    """
    SHAPE_CHOICES = (
        ('r', 'Rectangular'),
        ('t', 'Triangular')
    )
    name = models.CharField(max_length=200)
    shape = models.CharField(max_length=1, choices=SHAPE_CHOICES)
    base = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    pitch = models.DecimalField(max_digits=3, decimal_places=1)
    aspect = models.DecimalField(max_digits=3, decimal_places=1)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=9, decimal_places=7)