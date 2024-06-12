import pymongo

# Replace the connection string with your MongoDB URI
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the 'blog' database
db = client["blog"]

# Access the 'posts' collection
posts_collection = db["posts"]

new_post = {
    "title": "Introduction to MongoDB with PyMongo",
    "content" : "MongoDB is a NoSQL database. PyMongo is the offiial Python library",
    "author": "John Doe",
    "tags" : ["MongoDB", "PyMongo", "NoSQL"]

}

result = posts_collection.insert_one(new_post)
print(f"Inserted Document ID: {result.inserted_id}")

insertion_status = result.acknowledged
print(f"Your Status is: {insertion_status}")
