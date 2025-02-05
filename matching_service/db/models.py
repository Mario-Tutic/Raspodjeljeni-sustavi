from sqlmodel import SQLModel, Field
from datetime import datetime

class Match(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    driver_id: int = Field(foreign_key="driver.id")
    matched_at: datetime = Field(default_factory=datetime.utcnow)

from geoalchemy2 import Geometry
from sqlalchemy import Column


class Driver(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_location: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))