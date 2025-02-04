from sqlmodel import SQLModel, Field
from geoalchemy2 import Geometry
from sqlalchemy import Column
from datetime import datetime

class Driver(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_location: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))