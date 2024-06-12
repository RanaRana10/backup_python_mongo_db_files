import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# x = mycol.find_one()
# x = mycol.find()
# for x in x:
#     print(x)


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({"id": 10}):
  print(x)


  myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
  print(x)

mycol.create_index("my_field")


mycol.create_index("another_field", unique=True)