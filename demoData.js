//In a Mongo shell use ie: load("CouponCustomer/demoData.js")

db.createCollection("coupons", {"autoIndexId": "1", }),
db.createCollection("customers", {"autoIndexId": "1", }),

db.coupons.insertMany([
    { "id": "VrjnaCnxtcF", "status": "1", "value": "1"},
    { "id": "H2Bn26LmKs9", "status": "1", "value": "1"},
    { "id": "vTfw6ZNaQbv", "status": "0", "value": "1"},
    { "id": "YCDMkPKMsuz", "status": "0", "value": "1"},
    { "id": "sxZuV67d9d9", "status": "0", "value": "1"},
    { "id": "8QFftxtUnQV", "status": "0", "value": "1"},
    { "id": "j42EfJCAGYh", "status": "0", "value": "1"},
    { "id": "PZ4RJEjvezt", "status": "0", "value": "1"},
    { "id": "sny7cnDvcyA", "status": "0", "value": "1"},
    { "id": "ffTSdR22tE4", "status": "0", "value": "1"},
]),

db.customers.insertMany([
    { "firstname": "Jane", "lastname": "Doe", "email": "jane.doe@test.com", "coupons": [ "VrjnaCnxtcF", "H2Bn26LmKs9" ] },
    { "firstname": "Pleb", "lastname": "Noob", "email": "pleb.noob@test.com", "coupons": [ ] },
])