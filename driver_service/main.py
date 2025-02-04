from fastapi import FastAPI
from router.drivers import router as driver_router

app = FastAPI()

app.include_router(driver_router, prefix="/drivers", tags=["Drivers"])