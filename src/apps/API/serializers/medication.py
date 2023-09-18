from rest_framework import serializers
from ..model.medication import Medication


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "__all__"
        image = serializers.ImageField()


class MedicationUploadMedication(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = "name"
        image = serializers.ImageField()
