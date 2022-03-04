import copy
from datetime import datetime
from typing import Any


class OpenHours:
    """
    >>>  OpenHours({'days': [1,2,3,4,5,6], 'hours': [8,9,10,11,12]})
    """

    def __init__(self, config: dict[str, Any]):
        self._config = copy.deepcopy(config)

    @property
    def config(self) -> dict[str, Any]:
        return self._config

    @property
    def days(self) -> list[str]:
        return self._config.get("days", [])

    @property
    def hours(self) -> list[str]:
        return self._config.get("hours", [])

    def is_open(self, dt: datetime):
        if dt.isoweekday() not in self.days:
            return False
        if dt.hour not in self.hours:
            return False
        return True
