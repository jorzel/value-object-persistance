import pytest

from value_objects.money import Currency, CurrencyMismatched, Money


def test_money_initialization_with_value_and_currency():
    some_dollars = Money(1200, Currency.USD)

    assert some_dollars.value == 1200
    assert some_dollars.currency == Currency.USD


def test_adding_money_with_different_currency_raises_exception():
    some_dollars = Money(1200, Currency.USD)
    some_euro = Money(100, Currency.EUR)

    with pytest.raises(CurrencyMismatched):
        some_dollars.add(some_euro)


def test_adding_money_with_the_same_currency():
    some_dollars = Money(1200, Currency.USD)
    several_dollars = Money(100, Currency.USD)

    total = some_dollars.add(several_dollars)

    assert total.value == 1300
    assert total.currency == Currency.USD
