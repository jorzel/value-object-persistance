from models.shop import Item, Shop
from value_objects.money import Currency, Money


def test_shop_set_proper_email(db_session):
    email_address = "test_@test.pl"
    shop = Shop()
    db_session.add(shop)

    shop.email = email_address

    db_session.flush()
    assert (
        db_session.query(Shop).filter(Shop.email_address == email_address).first()
        is not None
    )


def test_shop_sell_thing_decrease_balance(db_session):
    shop = Shop(balance_currency=Currency.USD)
    item = Item(price=Money(value=100, currency=Currency.USD))
    item2 = Item(price=Money(value=120, currency=Currency.USD))
    db_session.add(shop)

    shop.sell_item(item)
    shop.sell_item(item2)

    db_session.flush()
    assert shop.balance_value == 220
