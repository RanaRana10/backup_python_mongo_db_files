import pymongo

# Connect to MongoDB (assuming it's running locally on the default port)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or switch to the database
mydatabase = client["multiple_user"]

# Create or switch to the collection
users_collection = mydatabase["users"]

# Query for the "man" document
query_man = {"name": "man"}
man_document = users_collection.find_one(query_man)

# Add a new age to the existing array
new_age = 35
# users_collection.update_one(query_man, {"$push": {"age": new_age}})
users_collection.update_one(query_man, {"$addToSet": {"age": new_age}})



# new_ages = [3325, 43436, 34547]
# users_collection.update_one(query_man, {"$push": {"age": {"$each": new_ages}}})


# Print the updated document
updated_man_document = users_collection.find_one(query_man)
print("Updated Man Document:", updated_man_document)
