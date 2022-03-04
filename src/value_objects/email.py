class InvalidEmail(Exception):
    pass


class Email:
    """
    >>>  Email("m.x@test.pl")
    """

    def __init__(self, value: str) -> None:
        if "@" not in value:
            raise InvalidEmail
        self._raw = value
        self._normalized = value.strip().lower()

    def __str__(self) -> str:
        return self._normalized

    __repr__ = __str__

    @property
    def address(self) -> str:
        return self._normalized

    @property
    def domain(self) -> str:
        return self._normalized.split("@")[1]
