from motor.motor_asyncio import AsyncIOMotorClient
import os

client = None
db = None

async def connect_to_mongo():
    global client, db
    client = AsyncIOMotorClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("MONGO_DB")]

async def close_mongo_connection():
    global client
    client.close()
