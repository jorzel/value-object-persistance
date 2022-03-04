import enum


class CurrencyMismatched(Exception):
    pass


class Currency(enum.Enum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"
    CHF = "CHF"


class Money:
    """
    >>>  Money(value=21, currency=Currency.USD)
    """

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
