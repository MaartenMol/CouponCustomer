import pymongo
from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

#print('hoi')
#print(customers.find())

jane = customers.find({'firstname': 'Jane'})
for i in jane:
    pprint(i)
#print(jane)