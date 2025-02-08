from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_session
from db.crud import find_closest_driver
from core.config import settings
import openrouteservice

# Initialize ORS client with your API key
#Creating client once at startup see how should you handle it like this(singletone) or like DI 
client = openrouteservice.Client(key=settings.ORS_KEY)

router = APIRouter()


@router.get("/match/")
def match_user_to_driver(user_lat: float, user_lon: float,destination_lat: float, destination_lon: float, session: Session = Depends(get_session),osr_client=client):
    driver = find_closest_driver(session,client, user_lat, user_lon,destination_lat,destination_lon)
    if driver:
        return {"driver_id": driver.id, "distance": driver.name}
    return {"message": "No drivers available"}
