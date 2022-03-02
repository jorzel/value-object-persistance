from models.shop import Shop


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
