from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["School_Management_2"]

students_collections = db["students"]
courses_collections = db["courses"]

database_names = client.list_database_names()
collections_names = db.list_collection_names()

# grade_10_students = students_collections.find({"grade": 10})

# for student in grade_10_students:
#     print(student)

# students_with_grade = students_collections.find({"grades": {"$exists": True}}).limit(2)
students_with_grade = students_collections.find({"grade": {"$exists": True}}).sort("_id",1).limit(20)
for _ in students_with_grade:
    print(_)


    