import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)

# mydict = { "name": "Peter", "address": "Lowstreet 27" }

# x = mycol.insert_one(mydict)

# print(x.inserted_id)



# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)

# print(x.inserted_ids)





myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "id": 1, "name": "John", "address": "Highway 37"},
  { "id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "id": 3, "name": "Amy", "address": "Apple st 652"},
  { "id": 4, "name": "Hannah", "address": "Mountain 21"},
  { "id": 5, "name": "Michael", "address": "Valley 345"},
  { "id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
  { "id": 7, "name": "Betty", "address": "Green Grass 1"},
  { "id": 8, "name": "Richard", "address": "Sky st 331"},
  { "id": 9, "name": "Susan", "address": "One way 98"},
  { "id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
  { "id": 11, "name": "Ben", "address": "Park Lane 38"},
  { "id": 12, "name": "William", "address": "Central st 954"},
  { "id": 13, "name": "Chuck", "address": "Main Road 989"},
  { "id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)


