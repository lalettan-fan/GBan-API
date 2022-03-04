from pymongo import MongoClient
from config import Configs

DATABASE_URL = Configs.MONGO_URL
SESSION_NAME = "GBAN_API"

class Mongo:
    cluster = MongoClient(DATABASE_URL)
    db = cluster[SESSION_NAME]