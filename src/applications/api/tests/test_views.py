import pytest
from api.models import Station
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.parametrize(
    "url_name, status_code",
    [
        ("station-list", 200),
        ("station-detail", 200),
        ("station-state", 200),
    ],
)
def test_views_statuses(create_station, client, url_name, status_code):
    station_id = Station.objects.last().id
    if url_name == "station-list":
        url = reverse(url_name)
    else:
        url = reverse(url_name, kwargs={"pk": station_id})
    response = client.get(url)

    assert response.status_code == status_code


@pytest.mark.django_db
@pytest.mark.parametrize(
    "axis, distance, state, value",
    [
        ("x", -50, "Running", 50),
        ("y", 50, "Running", 150),
        ("z", -10, "Running", 90),
        ("x", -101, "Broken", -1),
        ("y", -1000, "Broken", -900),
        ("z", -150, "Broken", -50),
    ],
)
def test_station_state(
    create_station, admin_client, create_user, axis, distance, state, value
):
    station = Station.objects.last()
    url_detail = reverse("station-detail", kwargs={"pk": station.id})
    url_state = reverse("station-state", kwargs={"pk": station.id})
    response_detail = admin_client.get(url_detail)
    response_state = admin_client.get(url_state)
    assert response_state.data["x"] == 100
    assert response_state.data["y"] == 100
    assert response_state.data["z"] == 100
    assert response_state.status_code == 200
    assert response_detail.status_code == 200
    assert response_detail.data["state"] == "Running"

    data = {
        "axis": axis,
        "distance": distance,
    }

    admin_client.post(url_state, data=data)
    station = Station.objects.last()
    assert station.state == state
    assert station.__getattribute__(axis) == value


@pytest.mark.django_db
def test_fail_response(create_station, admin_client):
    station = Station.objects.last()
    url_state = reverse("station-state", kwargs={"pk": station.id})
    data = {
        "axis": 100,
        "distance": "x",
    }
    response = admin_client.post(url_state, data=data)
    assert response.status_code == 400
