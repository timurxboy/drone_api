from django.contrib import admin

from src.apps.API.model.dron_card_item import DroneCardItem
from src.apps.API.model.drone import Drone
from src.apps.API.model.drone_card import DroneCard
from src.apps.API.model.medication import Medication


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = (
        "serial_number",
        "drone_model",
        "weight_limit",
        "battery_capacity",
        "state",
    )
    list_display_links = (
        "serial_number",
    )


@admin.register(Medication)
class DroneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "weight",
        "code",
        "image",
    )


@admin.register(DroneCard)
class DroneCardAdmin(admin.ModelAdmin):
    list_display = [
        "drone",
    ]


@admin.register(DroneCardItem)
class DroneCardItemAdmin(admin.ModelAdmin):
    list_display = (
        "drone_card",
        "medicament",
        "quantity",
    )
