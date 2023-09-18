from rest_framework import serializers
from ..model.dron_card_item import DroneCardItem
from ..model.drone_card import DroneCard


class DroneCardItemSerializer(serializers.ModelSerializer):
    drone_serial_number = serializers.CharField()

    class Meta:
        model = DroneCardItem
        fields = ("drone_serial_number", "medicament", "quantity",)

    def create(self, validated_data):
        serial_number = validated_data.pop("drone_serial_number")
        drone_card = DroneCard.objects.get(drone__serial_number=serial_number)
        instance = DroneCardItem.objects.create(drone_card=drone_card, **validated_data)
        return instance
