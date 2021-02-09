from fastapi import FastAPI

from app.routers.user import router as user_router

app = FastAPI()

app.include_router(user_router, tags=["User"], prefix="/user")


@app.get("/")
async def root():
    return {"message": "Welcome to my FastAPI app :)"}
