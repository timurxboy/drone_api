from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import Response
from ..model.drone import Drone
from ..serializers.check_battery import CheckBatterySerializer


class CheckBatteryView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        serial_number = kwargs.get('serial_number')
        drone = get_object_or_404(Drone, serial_number=serial_number)
        serializer = CheckBatterySerializer(drone)
        return Response(serializer.data)
