from pydantic_settings import BaseSettings
from pymongo import MongoClient

class Settings(BaseSettings):
    DATABASE_URL: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "covid_db"

settings = Settings()

def get_database():
    client = MongoClient(settings.DATABASE_URL)
    return client[settings.DATABASE_NAME]

def get_collection(collection_name: str):
    db = get_database()
    return db[collection_name]