from decimal import Decimal

from django.db import models
from django.core import validators


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
    # Width of planar surface.
    base = models.DecimalField(
        max_digits=5, decimal_places=2,
        validators=[
            validators.MinValueValidator(
                limit_value=Decimal('0'),
                message="Base measurement cannot be less than zero meters."
            ),
            validators.MaxValueValidator(
                limit_value=Decimal('999.99'),
                message="Base measurement cannot exceed 999.99 meters."
            )
        ]
    )
    # Height of the planar surface, perpendicular to the base.
    height = models.DecimalField(
        max_digits=4, decimal_places=2,
        validators=[
            validators.MinValueValidator(
                limit_value=Decimal('0'),
                message="Height cannot be less than zero meters."
            ),
            validators.MaxValueValidator(
                limit_value=Decimal('99.99'),
                message="Height measurement cannot exceed 99.99 meters."
            )
        ]
    )
    pitch = models.DecimalField(
        max_digits=3, decimal_places=1,
        validators=[
            validators.MinValueValidator(
                limit_value=Decimal('0'),
                message="Pitch cannot be less than zero degrees."
            ),
            validators.MaxValueValidator(
                limit_value=Decimal('75'),
                message="Pitch cannot exceed 75 degrees."
            )
        ]
    )
    aspect = models.DecimalField(
        max_digits=4, decimal_places=1,
        validators=[
            validators.MinValueValidator(
                limit_value=Decimal('0'),
                message="Aspect cannot be less than zero degrees."
            ),
            validators.MaxValueValidator(
                limit_value=Decimal('360'),
                message="Aspect cannot exceed 360 degrees."
            )
        ]
    )
    longitude = models.DecimalField(
        max_digits=10, decimal_places=7,
        validators=[
            validators.MinValueValidator(
                limit_value=Decimal('-180'),
                message='Longitude cannot be less than -180 degrees.'
            ),
            validators.MaxValueValidator(
                limit_value=Decimal('180'),
                message='Longitude cannot exceed 180 degrees.'
            )
        ]
    )
    latitude = models.DecimalField(
        max_digits=9, decimal_places=7,
        validators=[
            validators.MinValueValidator(
                limit_value=Decimal('-90'),
                message="Latitude may not be less than -90 degrees."
            ),
            validators.MaxValueValidator(
                limit_value=Decimal('90'),
                message="Latitude may not exceed 90 degrees."
            )
        ]
    )