import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

all_customers.encode('utf8') = customers.find()
for i in all_customers:
    pprint(i)