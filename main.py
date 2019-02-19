import pymongo
from pymongo import MongoClient
from pprint import pprint
import json
import sys

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

all_customers = customers.find()
for i in all_customers:
    pprint convert(i)