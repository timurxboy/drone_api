from rest_framework import serializers
from ..model.drone import Drone


class CheckingStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ["serial_number"]
