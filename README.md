# value-object-persitance
Value object persistent strategies using SQLalchemy ORM

# Simple field
```python
# value_objects/email.py

class InvalidEmail(Exception):
    pass


class Email:
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


# models/shop.py

from typing import Optional

from value_objects.email import Email


class Shop:
    def __init__(self):
        self.email_address: Optional[str] = None

    @property
    def email(self) -> Optional[Email]:
        return Email(self.email_address)

    @email.setter
    def email(self, email_address: str) -> None:
        self.email_address = Email(email_address).address


# orm.py
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import mapper

from db import metadata
from models.shop import Shop

shop = Table(
    "shop",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email_address", String),
)


def run_mappers():
    """
    Provides mapping between db tables and domain models.
    """

    mapper(Shop, shop)

```
