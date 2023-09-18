from rest_framework import permissions
from rest_framework import generics
from src.apps.API.model.medication import Medication
from src.apps.API.serializers.medication import MedicationSerializer
from rest_framework.parsers import MultiPartParser
from rest_framework.views import Response


class MedicationRegisterView(generics.CreateAPIView):
    serializer_class = MedicationSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Medication.objects.all()
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=400)
