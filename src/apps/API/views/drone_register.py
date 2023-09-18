from rest_framework import permissions
from rest_framework import generics
from src.apps.API.model.drone import Drone
from src.apps.API.serializers.drone import DroneSerializer


class DroneRegisterView(generics.CreateAPIView):
    serializer_class = DroneSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Drone.objects.all()