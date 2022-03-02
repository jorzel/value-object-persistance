# value-object-persitance
Value object persistent strategies using SQLalchemy ORM

## Simple field
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

## Composite field

```python
# value_objects/money.py
import enum

class CurrencyMismatched(Exception):
    pass

class Currency(enum.Enum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"
    CHF = "CHF"

class Money:
    def __init__(self, value: int, currency: Currency):
        self._value = value
        self._currency = currency

    def __composite_values__(self):
        return self._value, self._currency

    @property
    def currency(self) -> Currency:
        return self._currency

    @property
    def value(self) -> int:
        return self._value

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise CurrencyMismatched
        return Money(self.value + other.value, self.currency)


# models/shop.py
from typing import Optional

from value_objects.money import Currency, Money


class Item:
    def __init__(self, price: Money):
        self.price = price


class Shop:
    def __init__(self, balance_currency: Optional[Currency] = Currency.USD):
        if not balance_currency:
            balance_currency = Currency.USD
        self.balance = Money(0, balance_currency)

    def sell_item(self, item: Item) -> None:
        self.balance = self.balance.add(item.price)

# orm.py
from sqlalchemy import Column, Enum, Integer, Table
from sqlalchemy.orm import composite, mapper

from db import metadata
from models.shop import Currency, Shop
from value_objects.money import Money

shop = Table(
    "shop",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("balance_value", Integer, default=0, nullable=False),
    Column("balance_currency", Enum(Currency), default=Currency.USD, nullable=False),
)


def run_mappers():
    """
    Provides mapping between db tables and domain models.
    """

    mapper(
        Shop,
        shop,
        properties={
            "balance": composite(Money, shop.c.balance_value, shop.c.balance_currency)
        },
    )

```
