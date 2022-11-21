import pytest
from api.models import Pointer
from api.models import Station
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def create_user(db):
    return User.objects.create_user("user", "user@mail.com", "password")


@pytest.fixture()
def create_station(db):
    return Station.objects.create(name="TestStation")


@pytest.fixture
def create_pointer(db, create_user):
    return Pointer.objects.create(user=create_user, distance=100, axis="x")
