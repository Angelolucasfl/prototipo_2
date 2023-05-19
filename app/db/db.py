from motor.motor_asyncio import AsyncIOMotorClient
#from app.schemas.schemas import Filme

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)
db = client["movie_db"]

collection = db["filmes"]










#metodo alternativo
'''
async def add_filme(filme):
    document = filme
    result = await collection.insert_one(document)
    return document
'''
