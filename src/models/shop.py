from typing import Optional

from value_objects.email import Email
from value_objects.location import Location
from value_objects.money import Currency, Money
from value_objects.open_hours import OpenHours


class Item:
    def __init__(self, price: Money):
        self.price = price


class Shop:
    def __init__(
        self,
        balance_currency: Currency = Currency.USD,
        location: Optional[Location] = None,
        open_hours_config: Optional[dict] = None,
    ):
        self.email_address: Optional[str] = None
        if not balance_currency:
            balance_currency = Currency.USD
        self.balance = Money(0, balance_currency)
        self.location = location
        if not open_hours_config:
            open_hours_config = {}
        self.open_hours_config = open_hours_config

    @property
    def email(self) -> Optional[Email]:
        return Email(self.email_address)

    @email.setter
    def email(self, email: Email) -> None:
        self.email_address = email.address

    @property
    def open_hours(self) -> OpenHours:
        return OpenHours(self.open_hours_config)

    @open_hours.setter
    def open_hours(self, open_hours: OpenHours) -> None:
        self.open_hours_config = open_hours.config

    def sell_item(self, item: Item) -> None:
        self.balance = self.balance.add(item.price)
