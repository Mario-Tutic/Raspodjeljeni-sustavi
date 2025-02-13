from pydantic import BaseModel
from typing import Literal
import uuid

class MatchStatus(BaseModel):
    offer_id: uuid.UUID
    status:Literal["accepted","refused"]