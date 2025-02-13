from sqlmodel import Session, select
from shapely.geometry import Point
from geoalchemy2.functions import ST_Distance
#from db.models import Match
from .models import Driver  # Assuming driver model is in another service
from .models import RideOffer
from sqlalchemy import func
import openrouteservice
from core.config import settings




#I SHOULD HAVE SPATIAL INDEXING ON GEOM COLUMN !!!!!
def find_ride_info(session: Session,
                        osr_client, 
                        user_lat: float, user_lon: float,
                        destination_lat: float, destination_lon: float, radius: int=5000):
    
    #convert locations to wkb
    user_location = func.ST_SetSRID(func.ST_MakePoint(user_lon, user_lat), 4326)
    destination_location = func.ST_SetSRID(func.ST_MakePoint(destination_lon, destination_lat), 4326)

    #Find all driver within 5km and order by distance from client
    query = (
        select(Driver)
        .where(func.ST_DWithin(Driver.last_location, user_location, radius))
        .order_by(func.ST_Distance(Driver.last_location, user_location))
        .limit(1)
    )
    
    closest_driver = session.exec(query).first()

    #Cordinates format to proccede to OSR client
    coords = ((user_lon,user_lat), (destination_lon,destination_lat))

    # Get driving route
    #radiuses=[50, 50]  # Limit search to roads within 50 meters of input points
    route = osr_client.directions(coords, profile='driving-car',preference="recommended")
    distance_km = route['routes'][0]['summary']['distance'] / 1000  # Convert to km
    duration_min = route['routes'][0]['summary']['duration'] / 60  # Convert to minutes
    print(f"\n \n Driving Distance: {distance_km:.2f} km, Duration: {duration_min:.1f} min")
    print(route)

    #CALCULATING SNAPPED START AND END LOCATION(IF LOCATIONS ARE A BIT FURTHER FROM ROADS)
    
    ride_offer = RideOffer(time=duration_min,distance=distance_km,start_location=user_location,end_location=destination_location,)
    session.add(ride_offer)
    session.commit()

    
    return ride_offer