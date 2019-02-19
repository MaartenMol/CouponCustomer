#Import needed modules
import pymongo
from pymongo import MongoClient
from pprint import pprint
import sys
import collections

#Setup MongoDB Conn
client = MongoClient()
db = client.test
customers = db.customers
coupons = db.coupons

#Convert a dict to UTF8
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def searchCustomer(column, keyWord):
    foundCustomers = customers.find({ {}: "{}" }.format(column, keyWord))
    for i in foundCustomers:
        i = convert(i)
        pprint(i)

#Print all customers
#all_customers = customers.find()
#for i in all_customers:
#    i = convert(i)
#    pprint(i)

searchCustomer("firstname", "Jane")