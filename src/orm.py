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
