from sqlalchemy import select

from models.shop import Item, Shop
from value_objects.email import Email
from value_objects.location import Location
from value_objects.money import Currency, Money


def test_shop_set_proper_email(db_session):
    email_address = "test_@test.pl"
    shop = Shop()
    db_session.add(shop)

    shop.email = Email(email_address)

    db_session.flush()
    shop_table = Shop.__table__
    assert (
        db_session.execute(
            select(shop_table).where(shop_table.c.email_address == email_address)
        ).first()
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


def test_shop_set_location(db_session):
    shop = Shop(balance_currency=Currency.USD)
    location = Location(city="T", region="W", longitude=21.02, latitude=22.11)
    db_session.add(shop)
    db_session.add(location)
    db_session.flush()

    shop.location = location

    db_session.flush()
    location_table = Location.__table__
    shop_table = Shop.__table__

    assert (
        db_session.execute(
            select(location_table).where(
                location_table.c.city == "T",
                location_table.c.region == "W",
                location_table.c.longitude == 21.02,
                location_table.c.latitude == 22.11,
            )
        ).first()
        is not None
    )
    assert (
        db_session.execute(
            select(shop_table).where(shop_table.c.location_id == location.id)
        ).first()
        is not None
    )
