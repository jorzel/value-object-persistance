from sqlalchemy import Column, Enum, Integer, String, Table
from sqlalchemy.orm import composite, mapper

from db import metadata
from models.shop import Currency, Shop
from value_objects.money import Money

shop = Table(
    "shop",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email_address", String),
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
