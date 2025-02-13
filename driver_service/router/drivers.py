from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from db.session import get_session
from db.crud import update_driver_location
from db.models import Driver
import uuid


router = APIRouter()

@router.post("/update_location",response_model=Driver)
def update_location(driver_id: uuid.UUID, lat: float, lon: float, session: Session = Depends(get_session)):
    return update_driver_location(session, driver_id, lat, lon)


#EXPLOR WHAT IS AsyncSession !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#lets say this is part of registration/login and user sens an fcm token
#also check for how long it lasts
@router.post("/register_fcm_token/")
async def register_fcm_token(driver_id: int, fcm_token: str, session: Session = Depends(get_session)):
    driver = await session.get(Driver, driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")

    driver.fcm_token = fcm_token
    await session.commit()
    return {"message": "FCM token registered"}