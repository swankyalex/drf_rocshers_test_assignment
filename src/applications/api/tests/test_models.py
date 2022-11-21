from datetime import datetime

import pytest
from api.models import Pointer
from api.models import Station
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_create(create_user):
    """Test user creation"""
    user = User.objects.last()
    assert user.name == "user"
    assert user.email == "user@mail.com"
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_create_station(create_station):
    """Test Station Creation"""
    station = Station.objects.last()
    assert station.name == "TestStation"
    assert station.x == 100
    assert station.y == 100
    assert station.z == 100
    assert station.state == "Running"
    assert isinstance(station.time_create, datetime)
    assert station.time_broke is None
    assert Station.objects.count() == 1
    assert str(station) == "TestStation"


@pytest.mark.django_db
def test_create_pointer(create_user, create_pointer):
    """Test"""
    pointer = Pointer.objects.last()
    assert pointer.distance == 100
    assert pointer.axis == "x"
    assert Pointer.objects.count() == 1
    assert pointer.user.name == "user"
    assert str(pointer) == "By user on x axis for 100 points"
