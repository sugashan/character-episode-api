from pymongo import MongoClient
import os

client = None

def init_db():
    global client
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    client = MongoClient(mongo_uri)
    print("Database connected!")

def get_db():
    if client is None:
        raise Exception("Database not initialized")
    return client['character_cards']
