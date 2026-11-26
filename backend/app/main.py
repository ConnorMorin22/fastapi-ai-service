from fastapi import FastAPI
from . import routers


app = FastAPI()

app.include_router(routers.router)

@app.get('/')
async def api_validation():
    return {"message": "API is running..."}

