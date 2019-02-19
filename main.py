import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

#print('hoi')
#print(customers.find())

all_customers = customers.find()
print(all_customers)