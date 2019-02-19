import pymongo
import pprint
from pymongo import MongoClient

client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

print('hoi')
print(db.customers.find().pretty())
pprint.pprint(db.customers.find().pretty())
pprint.pprint(coupons.find())

