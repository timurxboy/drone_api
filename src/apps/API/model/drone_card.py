from django.db import models
from django.db.models.signals import post_save
from .drone import Drone
from django.dispatch import receiver


class DroneCard(models.Model):
    drone = models.OneToOneField(Drone, on_delete=models.CASCADE, related_name='drone_card')
    available = models.PositiveSmallIntegerField()

    def get_items_quantity(self):
        return self.drone_card_items.count()

    def __str__(self):
        return self.drone.serial_number

    @receiver(post_save, sender=Drone)
    def create_drone_card(sender, instance, created, **kwargs):
        if created:
            DroneCard.objects.create(drone=instance, available=instance.weight_limit)

    post_save.connect(create_drone_card, sender=Drone)
