from .models import Device
from rest_framework import serializers

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ("last_edited", "type", "device_id")