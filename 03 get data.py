import pymongo

# Connect to MongoDB (assuming it's running locally on the default port)
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydatabase = client["multiple_user"]
users_collection = mydatabase["users"]

# Query for the "man" document
query_man = {"name": "man"}
man_document = users_collection.find_one(query_man)

# Get the 'age' array from the document
man_ages = man_document.get('age', [])

# Print all ages
print("Ages of Man:", man_ages)

print(type(man_ages))