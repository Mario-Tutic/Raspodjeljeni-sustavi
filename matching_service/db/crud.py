from sqlmodel import Session, select
from shapely.geometry import Point
from geoalchemy2.functions import ST_Distance
#from db.models import Match
from .models import Driver  # Assuming driver model is in another service
from .models import RideOffer
from sqlalchemy import func
import openrouteservice
from core.config import settings
from sqlalchemy.exc import SQLAlchemyError
from geoalchemy2.shape import from_shape




#I SHOULD HAVE SPATIAL INDEXING ON GEOM COLUMN !!!!!
def find_ride_info(session: Session,
                        osr_client, 
                        user_lat: float, user_lon: float,
                        destination_lat: float, destination_lon: float, radius: int=5000):
    
    #convert locations to wkb

    user_location = from_shape(Point(user_lon, user_lat), srid=4326)
    destination_location = from_shape(Point(destination_lon, destination_lat), srid=4326)

    #Find all drivers within 5km and order by distance from client
    query = (
        select(Driver)
        .where(func.ST_DWithin(Driver.last_location, user_location, radius))
        .order_by(func.ST_Distance(Driver.last_location, user_location))
        .limit(1)
    )
    
    closest_driver = session.exec(query).first()

    #Cordinates format to proccede to OSR client
    coords = ((user_lon,user_lat), (destination_lon,destination_lat))
    #print(f"\n\nCORDS:{coords}")

    # Get driving route
    #radiuses=[50, 50]  # Limit search to roads within 50 meters of input points
    route = osr_client.directions(coords, profile='driving-car',preference="recommended")
    distance_km = route['routes'][0]['summary']['distance'] / 1000  # Convert to km
    duration_min = route['routes'][0]['summary']['duration'] / 60  # Convert to minutes
    print(f"\n \n Driving Distance: {distance_km:.2f} km, Duration: {duration_min:.1f} min")
    #print(route)

    #CALCULATING SNAPPED START AND END LOCATION(IF LOCATIONS ARE A BIT FURTHER FROM ROADS)

    ride_offer = RideOffer(time=duration_min, distance=distance_km, start_location=user_location, end_location=destination_location,price=2*distance_km, driver_id=closest_driver.id)

    try:   
        session.add(ride_offer)
        session.commit()
    except SQLAlchemyError as e:
        print(f"Error while committing to the database: {e}")

    ride_offer.start_location=str(ride_offer.start_location)
    ride_offer.end_location=str(ride_offer.end_location)

    #driver.last_location = session.scalar(func.ST_AsText(driver.last_location))
    #driver.last_location=str(driver.last_location)
    
    return ride_offer