
import databases
import sqlalchemy
import datetime
from sqlalchemy import Column, Integer, DateTime

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./async_test.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

clusters = sqlalchemy.Table(
    "clusters3",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("config", sqlalchemy.String),
    sqlalchemy.Column("status", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
