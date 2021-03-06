from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URI = "sqlite:///"

engine = create_engine(SQLALCHEMY_DATABASE_URI)
metadata = MetaData(bind=engine)
Base = declarative_base(metadata=metadata)


from orm import run_mappers

run_mappers()
