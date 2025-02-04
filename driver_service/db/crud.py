from sqlmodel import Session
from geoalchemy2.shape import from_shape
from shapely.geometry import Point
from datetime import datetime
from db.models import Driver

def update_driver_location(session: Session, driver_id: int, lat: float, lon: float):
    point = from_shape(Point(lon, lat), srid=4326)

    # Update last location in Driver table
    driver = session.get(Driver, driver_id)
    if driver:
        driver.last_location = point
        session.add(driver)

    session.commit()
    
    return driver