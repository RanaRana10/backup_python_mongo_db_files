from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

database_names = client.list_database_names()

db = client["School_Management_2"]

students_collections = db["students"]
courses_collections = db["courses"]


query = {"name": "Bob"}
new_values = {"$set": {"phone": [343354]}}

students_collections.update_one(query, new_values)