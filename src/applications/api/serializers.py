from rest_framework import serializers

from .models import Pointer
from .models import Station


class StationListSerializer(serializers.ModelSerializer):
    """Serializer for ListView of ships"""

    class Meta:
        model = Station
        exclude = ("x", "y", "z")
        read_only_fields = ("state", "time_create", "time_broke")


class StationStateSerializer(serializers.ModelSerializer):
    """Serializer for checking state of ship"""

    class Meta:
        model = Station
        fields = ("x", "y", "z")


class PointerSerializer(serializers.ModelSerializer):
    """Serializer for Pointers"""

    class Meta:
        model = Pointer
        fields = "__all__"
        read_only_fields = ["user"]
