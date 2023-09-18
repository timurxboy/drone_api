from django.core.validators import MinValueValidator
from django.db import models

from src.apps.API.model.drone_card import DroneCard
from src.apps.API.model.medication import Medication


class DroneCardItem(models.Model):
    drone_card = models.ForeignKey(DroneCard, on_delete=models.CASCADE, verbose_name='drone_card_items',
                                   related_name='drone_card_items')
    medicament = models.ForeignKey(Medication, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.medicament} {self.quantity}"
