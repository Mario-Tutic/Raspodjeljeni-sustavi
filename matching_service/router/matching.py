import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_session
from db.crud import find_ride_info
from core.config import settings
import openrouteservice
from fastapi import Path
from typing import Literal
from py_models.models import MatchStatus
from db.models import RideOffer, Driver

# Initialize ORS client with your API key

def get_OSR_client():
    client = openrouteservice.Client(key=settings.ORS_KEY)
    return client

router = APIRouter()


@router.get("/find-ride",response_model=RideOffer)
def find_ride(user_lat: float, user_lon: float,destination_lat: float, destination_lon: float, session: Session = Depends(get_session),osr_client:openrouteservice.Client=Depends(get_OSR_client)):
    ride_info = find_ride_info(session,osr_client, user_lat, user_lon,destination_lat,destination_lon)
    if ride_info:
        return ride_info
    return {"message": "No drivers available"}


#WRONG BUT USE FOR REFERENCE LATER
'''
@router.post("/confirm-ride/")
async def confirm_ride(ride_id: uuid.UUID, session: Session = Depends(get_session)):
    ride = await session.get(RideOffer, ride_id)
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")

    # Mark ride as confirmed
    ride.status = True
    await session.commit()

    # Get driver details
    driver = await session.get(Driver, ride.driver_id)
    if driver and driver.fcm_token:
        # Send FCM Notification
        send_fcm_notification(
            fcm_token=driver.fcm_token,
            title="New Ride Confirmed!",
            body=f"A user has confirmed a ride. Pickup at {ride.pickup_location}.",
            data_payload={"ride_id": ride_id, "status": "confirmed"}
        )

    return {"message": "Ride confirmed, driver notified!"}
'''



#SEND NOTIFICATION TO DRIVER TEST
import firebase_admin
from firebase_admin import credentials, messaging

# Initialize Firebase Admin SDK
cred = credentials.Certificate("core/uber-copy-254c5-firebase-adminsdk-fbsvc-9f8147c87f.json")
firebase_admin.initialize_app(cred)
 
@router.post("/confirm-ride/")
async def send_notification(token: str , id: uuid.UUID,session:Session = Depends(get_session)):
    #Mark ride as confirmed
    ride = session.get(RideOffer, id)
    if not ride:
        raise HTTPException(status_code=404, detail="Ride not found")
    ride.confirmed = True
    session.add(ride)
    session.commit()

    #Send a notification to a device using FCM token

  
    message = messaging.Message(
        notification=messaging.Notification(title="New Ride Confirmed!", body="You got a new ride"),
        token=token,
        data={"ride_id": str(id)}
    )

    try:
        response = messaging.send(message)
        return {"success": True, "response": response}
    except Exception as e:
        return {"success": False, "error": str(e)}
