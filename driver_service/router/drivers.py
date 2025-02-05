from fastapi import APIRouter, Depends
from sqlmodel import Session
from db.session import get_session
from db.crud import update_driver_location
from db.models import Driver

router = APIRouter()

@router.post("/update_location",response_model=Driver)
def update_location(driver_id: int, lat: float, lon: float, session: Session = Depends(get_session)):
    return update_driver_location(session, driver_id, lat, lon)