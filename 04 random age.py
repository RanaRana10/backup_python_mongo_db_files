import pymongo
import random

# Connect to MongoDB (assuming it's running locally on the default port)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or switch to the database
mydatabase = client["multiple_user"]

# Create or switch to the collection
users_collection = mydatabase["users"]

# Query for the "man" document
query_man = {"name": "man"}
man_document = users_collection.find_one(query_man)

# Get the 'age' array from the document
man_ages = man_document.get('age', [])

# Print all ages
print("Ages of Man:", man_ages)

# Get a random age from the list
random_age = random.choice(man_ages)

# Print the random age
print("Random Age:", random_age)
