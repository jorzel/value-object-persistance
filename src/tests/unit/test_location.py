import pytest

from value_objects.location import InvalidGeolocation, Location


def test_location_initialization_succeed_when_values_are_valid():
    location = Location(city="X", region="Y", latitude=21.91, longitude=28.20)

    assert location.city == "X"
    assert location.region == "Y"
    assert location.latitude == 21.91
    assert location.longitude == 28.20


def test_location_initialization_raises_exception_when_geolocation_is_below_zero():
    with pytest.raises(InvalidGeolocation):
        _ = Location(city="X", region="Y", latitude=21.91, longitude=-28.20)
