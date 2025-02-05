from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_session
from db.crud import find_closest_driver

router = APIRouter()

@router.get("/match/")
def match_user_to_driver(lat: float, lon: float, session: Session = Depends(get_session)):
    driver = find_closest_driver(session, lat, lon)
    if driver:
        return {"driver_id": driver.id, "distance": driver.name}
    return {"message": "No drivers available"}
