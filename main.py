import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

pprint.pprint(customers.find().pretty())
pprint.pprint(coupons.find().pretty())