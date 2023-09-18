from rest_framework import generics
from rest_framework.views import Response
from src.apps.API.model.drone_card import DroneCard


class CleanCardItemsView(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        card = DroneCard.objects.get(drone__serial_number=kwargs['serial_number'])
        card.drone_card_items.all().delete()
        card.available = card.drone.weight_limit
        card.save()
        return Response({"message": "Cart has been cleared successfully."}, status=204)
