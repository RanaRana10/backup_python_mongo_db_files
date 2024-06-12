import pymongo

# Connect to MongoDB (assuming it's running locally on the default port)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or switch to the database
mydatabase = client["multiple_user"]

# Create or switch to the collection
users_collection = mydatabase["users"]

# Insert documents with multiple values for the 'age' field
user1 = {"name": "man", "age": [30, 31, 33]}
user2 = {"name": "woman", "age": [23, 33]}

users_collection.insert_one(user1)
users_collection.insert_one(user2)


