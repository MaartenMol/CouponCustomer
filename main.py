import pymongo
from pymongo import MongoClient
from pprint import pprint
import json

client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

all_customers = customers.find()
for i in all_customers:
    #pprint(i)
    json.dump(i, sys.stdout)