from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]
collection = db["mycollection"]

document = {"_id": "ObjectId(04)","id": 1.5,"name" : "Manik Kumar Rana", "age" : 22, "city" : "Kalinagar"}
result = collection.update_one(document)

print(f"Document inserted with ID: {result.inserted_id}")


documents = [
    {"name" : "Alice", "age": 25, "city": "London"},
    {"name": "Bob", "age": 30, "city": "Paris"},
    {"name": "Charlie", "age": 28, "city": "Barlin"}

]

# result = collection.insert_many(documents)





