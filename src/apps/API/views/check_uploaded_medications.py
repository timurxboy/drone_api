from rest_framework import generics, permissions
from rest_framework.views import Response
from ..model.dron_card_item import DroneCardItem


class CheckUploadedMedications(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        drone_card_item = DroneCardItem.objects.filter(drone_card__drone__serial_number=kwargs["serial_number"],
                                                       medicament__id=kwargs["medication_id"])

        if drone_card_item.exists():
            return Response({"status": True}, status=400)

        return Response({"status": False}, status=200)
