from rest_framework import generics
from rest_framework.views import Response
from ..model.dron_card_item import DroneCardItem
from ..serializers.loaded_medications_on_drone import LoadedMedicationsOnDroneSerializer


class LoadedMedicationsOnDroneView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        serial_number = DroneCardItem.objects.filter(drone_card__drone__serial_number=kwargs['serial_number'])
        print(serial_number)
        serializer = LoadedMedicationsOnDroneSerializer(serial_number, many=True)
        return Response(serializer.data)
