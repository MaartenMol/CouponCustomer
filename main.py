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

posts = db.posts

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

#Search customers
def searchCustomer(column, keyWord):
    foundCustomers = customers.find({ column: keyWord })
    for i in foundCustomers:
        i = convert(i)
        pprint(i)

#Search coupons
def searchCoupons(column, keyWord):
    foundCoupons = coupons.find({ column: keyWord })
    for i in foundCoupons:
        i = convert(i)
        pprint(i)

#Add coupons
#Status 0 = unregistrered, 1 = registrered to user, 2 = used by user
def addCoupons(id, status, value):
    postData = { "id": id, "status": status, "value": value }
    result = coupons.insert_one(postData)
    print('Added Coupon: {0}'.format(result.inserted_id))

#Print all customers
#all_customers = customers.find()
#for i in all_customers:
#    i = convert(i)
#    pprint(i)

pprint("Zoeken naar Jane")
searchCustomer("firstname", "Jane")
pprint("Zoeken naar alle ongeregistreerde coupons")
searchCoupons("status", "0")
pprint("Zoeken naar alle coupons van Jane")
searchCoupons("customer_id", "5c6c1d49a990cde0ca31a23e")
#pprint("Voeg coupon toe")
#addCoupons("hyvgpHWenqM", "0", "1")