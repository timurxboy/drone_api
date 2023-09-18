from rest_framework import generics
from rest_framework.views import Response
from ..model.drone import Drone
from ..serializers.checking_stats import CheckingStateSerializer


class CheckingStateView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        drone = Drone.objects.filter(state='IDLE')
        print(drone)
        serializer = CheckingStateSerializer(drone, many=True)
        return Response(serializer.data)
