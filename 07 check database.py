from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["School_Management_2"]

students_collections = db["students"]
courses_collections = db["courses"]

database_names = client.list_database_names()
collections_names = db.list_collection_names()


print(database_names)
print(collections_names)




students_data = students_collections.find({})

for document in students_data:
    print(document)

course_data = courses_collections.find({})

for document in course_data:
    print(document)