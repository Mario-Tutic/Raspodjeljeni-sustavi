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



#WILL BE STORED AS TEMPORARY DATA INSIDE DATABASE UNTIL USER CONFIRMS
class RideOffer(SQLModel,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    time:float#minutes
    distance:float#km
    start_location: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))
    end_location: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))
    price:float
    confirmed:bool = False
    timestamp:datetime = Field(default_factory=datetime.now)
    driver_id: uuid.UUID = Field(default=None,foreign_key="driver.id")
#CONFIRMED RIDE
'''
class Ride(SQLModel,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id")
    driver_id: uuid.UUID = Field(foreign_key="driver.id")
    start_location: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))
    end_location: str = Field(sa_column=Column(Geometry("POINT", srid=4326)))
'''
class User(SQLModel,table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name:str
    surname:str
