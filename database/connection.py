import pymongo
import settings as settings
import os

db = None
try:
    client = pymongo.MongoClient(settings.mongodb_uri, settings.port)
    client.server_info()
    db = client.localhost
except pymongo.errors.ServerSelectionTimeoutError as err:
    print("DB connection not done.",err)