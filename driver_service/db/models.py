from sqlmodel import SQLModel, Field
from geoalchemy2 import Geometry
from sqlalchemy import Column
from datetime import datetime
import uuid

class Driver(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str
    surname:str
    last_location: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))
    fcm_token: str = Field(default=None, nullable=True)  # Store FCM token (optional field)