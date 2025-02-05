from fastapi import FastAPI
from router.matching import router

app = FastAPI()

app.include_router(router, tags=["Matching Service"])