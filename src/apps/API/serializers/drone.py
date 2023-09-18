from rest_framework import serializers
from ..model.drone import Drone
from ..model.drone_card import DroneCard


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = "__all__"


class DroneCardSerializer(serializers.ModelSerializer):
    drone = DroneSerializer()

    class Meta:
        model = DroneCard
        fields = '__all__'


class DroneUploadMedication(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ("serial_number",)
