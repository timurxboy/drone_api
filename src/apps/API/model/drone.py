from django.core.validators import MaxValueValidator
from django.db import models


class Drone(models.Model):
    MODEL_CHOICES = (
        ('LIGHTWEIGHT', 'Lightweight'),
        ('MIDDLEWEIGHT', 'Middleweight'),
        ('CRUISERWEIGHT', 'Cruiserweight'),
        ('HEAVYWEIGHT', 'Heavyweight'),
    )

    STATE_CHOICES = (
        ('IDLE', 'IDLE'),
        ('LOADING', 'LOADING'),
        ('LOADED', 'LOADED'),
        ('DELIVERING', 'DELIVERING'),
        ('DELIVERED', 'DELIVERED'),
        ('RETURNING', 'RETURNING'),
    )

    serial_number = models.CharField(max_length=100, unique=True, primary_key=True)
    drone_model = models.CharField(max_length=15, choices=MODEL_CHOICES)
    weight_limit = models.PositiveSmallIntegerField(validators=[MaxValueValidator(500)])
    battery_capacity = models.PositiveSmallIntegerField(validators=[MaxValueValidator(100)])
    state = models.CharField(max_length=10, choices=STATE_CHOICES)

    def __str__(self):
        return self.serial_number
