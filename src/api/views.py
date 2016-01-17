from requests import Response
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from rest_framework.decorators import detail_route

from .models import TimeStampedModel, Device
from .serializers import DeviceSerializer


class DeviceView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    permission_classes = [permissions.AllowAny]

    def get_list(self, request, pk=None):
        queryset = Device.objects.none()

        if request.user.is_superuser:
            queryset = Device.objects.all()

        if pk is not None:
            queryset = Device.objects.get(device_id=pk)

        serializer = self.get_serializer(queryset)

        return Response(serializer.data)

