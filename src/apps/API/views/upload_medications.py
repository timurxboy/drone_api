from rest_framework import generics, permissions
from rest_framework.views import Response

from ..model.dron_card_item import DroneCardItem
from ..model.drone_card import DroneCard
from ..model.medication import Medication
from ..serializers.upload_medications import DroneCardItemSerializer


class UploadMedicationsView(generics.CreateAPIView):
    serializer_class = DroneCardItemSerializer
    permission_classes = [permissions.AllowAny, ]
    queryset = DroneCardItem.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serial_number = serializer.validated_data.get('drone_serial_number')
        name = serializer.validated_data.get('medicament')
        quantity = serializer.validated_data.get('quantity')
        drone = DroneCard.objects.get(drone__serial_number=serial_number)
        weight_limit = drone.available
        print(weight_limit)
        medication = Medication.objects.get(name=name)
        max_weight = medication.weight * quantity
        print(max_weight)
        if weight_limit < max_weight:
            return Response({"status": "Weight limit exceeded"}, status=400)

        drone_card_item = DroneCardItem()
        drone_card_item.drone_card = drone
        drone_card_item.medicament = medication
        drone_card_item.quantity = quantity
        drone_card_item.save()
        drone.available -= max_weight
        drone.save()
        return Response({"status": "Successfully added"}, status=201)
