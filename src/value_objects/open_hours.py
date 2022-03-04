from datetime import datetime
from typing import Any


class OpenHours:
    def __init__(self, config: dict[str, Any]):
        self._config = config

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
