from rest_framework import serializers
from ..model.dron_card_item import DroneCardItem
from ..serializers.medication import MedicationSerializer


class LoadedMedicationsOnDroneSerializer(serializers.ModelSerializer):
    medicament = MedicationSerializer()

    class Meta:
        model = DroneCardItem
        fields = ["medicament", "quantity"]
