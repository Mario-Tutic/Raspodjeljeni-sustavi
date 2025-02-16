from pydantic import BaseModel
from typing import Literal
import uuid

class FindRide(BaseModel):
    user_lat: float
    user_lon: float
    destination_lat: float
    destination_lon: float
    
class MatchStatus(BaseModel):
    offer_id: uuid.UUID
    status:Literal["accepted","refused"]