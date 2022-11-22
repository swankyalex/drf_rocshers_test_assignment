from drf_spectacular.utils import extend_schema_view
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Station
from .schema_extenders import extenders
from .serializers import PointerSerializer
from .serializers import StationListSerializer
from .serializers import StationStateSerializer


@extend_schema_view(**extenders)
class StationViewSet(viewsets.ModelViewSet):
    """CRUD of Station model"""

    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StationListSerializer
    queryset = Station.objects.order_by("id")

    @action(methods=["get", "post"], detail=True)
    def state(self, request, pk=None):
        """Additional action for pointer usage"""
        self.serializer_class = PointerSerializer
        station = self.get_object()
        if request.method == "GET":
            return Response(StationStateSerializer(station).data)
        elif request.method == "POST":
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                distance = serializer.validated_data["distance"]
                ax = serializer.validated_data["axis"]
                attr = station.__getattribute__(f"{ax}")
                attr += distance
                station.__setattr__(f"{ax}", attr)
                station.save()
                serializer.save(user=request.user)
                return Response({"x": station.x, "y": station.y, "z": station.z})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
