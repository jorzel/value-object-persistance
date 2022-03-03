class InvalidGeolocation(Exception):
    pass


class Location:
    def __init__(self, city: str, region: str, longitude: float, latitude: float):
        if longitude < 0 or latitude < 0:
            raise InvalidGeolocation
        self._city = city
        self._region = region
        self._longitude = longitude
        self._latitude = latitude

    @property
    def city(self) -> str:
        return self._city

    @property
    def region(self) -> str:
        return self._region

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def latitude(self) -> float:
        return self._latitude
