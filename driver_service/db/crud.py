from sqlmodel import Session
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from datetime import datetime
from sqlalchemy import func
from .models import Driver

def update_driver_location(session: Session, driver_id: int, lat: float, lon: float):
    point = from_shape(Point(lon, lat), srid=4326)

    # Update last location in Driver table
    driver = session.get(Driver, driver_id)
    #print(f"\n[Driver found: {driver.id}\n{driver.name}\n{driver.last_location}]") when i place print here no error 
    if driver:
        driver.last_location = point
        session.add(driver)
    session.commit()

    # Convert the WKBElement(well known binary) returned by Point to WKT(well know text) for serialization
    #driver.last_location = session.scalar(func.ST_AsText(driver.last_location))
    driver.last_location=str(driver.last_location)

    print(f"\n[Driver found: {driver.id}\n{driver.name}\n{driver.last_location}]") #when i place print here error occurs 
    
    return driver