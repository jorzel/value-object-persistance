import pytest
from sqlalchemy.orm import sessionmaker

from db import engine, metadata


@pytest.fixture(scope="session")
def db_connection():
    metadata.drop_all()
    metadata.create_all()
    connection = engine.connect()

    yield connection

    metadata.drop_all()
    engine.dispose()


@pytest.fixture
def db_session(db_connection):
    transaction = db_connection.begin()
    session = sessionmaker(bind=db_connection)
    session = session()

    yield session

    transaction.rollback()
    session.close()
