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

