from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import composite, registry, relationship

from db import metadata
from models.shop import Currency, Shop
from value_objects.location import Location
from value_objects.money import Money

mapper_registry = registry()

location = Table(
    "location",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("city", String),
    Column("region", String),
    Column("longitude", Float),
    Column("latitude", Float),
)

shop = Table(
    "shop",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email_address", String),
    Column("balance_value", Integer, default=0, nullable=False),
    Column("balance_currency", Enum(Currency), default=Currency.USD, nullable=False),
    Column("location_id", Integer, ForeignKey("location.id")),
)


def run_mappers():
    """
    Provides mapping between db tables and domain models.
    """

    mapper_registry.map_imperatively(
        Location,
        location,
        properties={
            "_city": location.c.city,
            "_region": location.c.region,
            "_latitude": location.c.latitude,
            "_longitude": location.c.longitude,
        },
    )
    mapper_registry.map_imperatively(
        Shop,
        shop,
        properties={
            "balance": composite(Money, shop.c.balance_value, shop.c.balance_currency),
            "location": relationship(Location),
        },
    )
