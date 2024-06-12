from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

database_names = client.list_database_names()

db = client["School_Management_2"]

students_collections = db["students"]
courses_collections = db["courses"]

student_document = {"name": "1st Rana", "grade":10, "age": 22}
course_document = {"title":"History", "teacher": "2nd Rana", "room": "Room 101"}

students_collections.insert_one(student_document)
courses_collections.insert_one(course_document)

client.close()