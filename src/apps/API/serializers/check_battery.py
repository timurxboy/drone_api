from rest_framework import serializers
from ..model.drone import Drone


class CheckBatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ["battery_capacity"]
