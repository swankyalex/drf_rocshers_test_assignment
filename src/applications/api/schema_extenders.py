from api.serializers import PointerSerializer
from api.serializers import StationStateSerializer
from drf_spectacular.utils import extend_schema

extenders = {
    "list": extend_schema(description="Returns all available stations."),
    "create": extend_schema(
        description="Expects field `name`, creates station and returns it."
    ),
    "retrieve": extend_schema(
        description="Action returns a single object selected by `id`."
    ),
    "update": extend_schema(
        description="Action updates single object selected by `id`"
    ),
    "partial_update": extend_schema(
        description="Partial update single object selected by `id`"
    ),
    "destroy": extend_schema(description="Delete single object selected by `id`"),
    "state": [
        extend_schema(request=PointerSerializer, responses=StationStateSerializer),
        extend_schema(
            description="Update state of single object selected by `id`.",
            methods=["POST"],
        ),
        extend_schema(
            description="Returns state of single object selected by `id`.",
            methods=["GET"],
        ),
    ],
}
