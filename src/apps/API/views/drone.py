from rest_framework import generics
from ..model.drone import Drone
from ..serializers.drone import DroneSerializer


class DroneView(generics.ListAPIView):
    serializer_class = DroneSerializer
    queryset = Drone.objects.all()
