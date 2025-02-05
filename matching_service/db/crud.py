from sqlmodel import Session, select
from shapely.geometry import Point
from geoalchemy2.functions import ST_Distance
from db.models import Match
from db.models import Driver  # Assuming driver model is in another service
from sqlalchemy import func, text


#I SHOULD HAVE SPATIAL INDEXING ON GEOM COLUMN !!!!!


def find_closest_driver(session: Session, user_lat: float, user_lon: float,radius: int=5000):
    user_location = func.ST_SetSRID(func.ST_MakePoint(user_lon, user_lat), 4326)
    
    # Find the closest driver using PostGIS ST_Distance
    #THIS SHOULD BE OPTIMIZED
    query = select(Driver).order_by(
        ST_Distance(Driver.last_location, user_location)
    ).limit(1)
    
    query2 = (
        select(Driver)
        .where(func.ST_DWithin(Driver.last_location, user_location, radius))
        .order_by(func.ST_Distance(Driver.last_location, user_location))
        .limit(1)
    )


    closest_driver = session.exec(query).first()
    
    return closest_driver