import motor.motor_asyncio
from os import getenv

USERNAME = getenv("USERNAME", "fastapi")
PASSWORD = getenv("PASSWORD", "fastapi")
DATABASE_HOST = getenv("DB_HOST", "fastapi")
DATABASE_NAME = getenv("DB_NAME", "fastapi")
MONGO_URI = "mongodb+srv://{}:{}@{}/{}?retryWrites=true&w=1".format(USERNAME, PASSWORD, DATABASE_HOST, DATABASE_NAME)

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

database = client[DATABASE_NAME]

user_collection = database.get_collection("user")

