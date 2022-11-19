from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import extend_schema_view
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Station
from .serializers import PointerSerializer
from .serializers import StationListSerializer
from .serializers import StationStateSerializer


@extend_schema_view(
    list=extend_schema(description="Returns all available stations."),
    create=extend_schema(
        description="Action expects the fields `name`, creates station and returns it."
    ),
    retrieve=extend_schema(
        description="Action returns a single object selected by `id`."
    ),
    update=extend_schema(description="Update single object selected by `id`"),
    partial_update=extend_schema(
        description="Partial update single object selected by `id`"
    ),
    destroy=extend_schema(description="Delete single object selected by `id`"),
)
class StationViewSet(viewsets.ModelViewSet):
    """CRUD of Station model"""

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StationListSerializer
    queryset = Station.objects.all()

    @extend_schema(
        description="Action returns state of single object selected by `id`.",
        methods=["GET"],
        request=PointerSerializer,
        responses=StationStateSerializer,
    )
    @extend_schema(
        description="Action for updating state of object selected by `id`.",
        methods=["POST"],
        request=PointerSerializer,
        responses=StationStateSerializer,
    )
    @action(methods=["get", "post"], detail=True)
    def state(self, request, pk=None):
        """Additional action for pointer usage"""
        self.serializer_class = PointerSerializer
        if request.method == "GET":
            station = Station.objects.get(pk=pk)
            return Response(StationStateSerializer(station).data)
        elif request.method == "POST":
            station = self.get_object()
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
