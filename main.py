import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.test
collection = db.inventory

pprint.pprint(collection.find_one())