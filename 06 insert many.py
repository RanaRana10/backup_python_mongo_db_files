from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["School_Management_2"]

students_collections = db["students"]
courses_collections = db["courses"]


student_documents = [
    {"name": "Alice", "grade":10, "age": 15},
    {"name": "Bob", "grade": 11, "age": 16},
    {"name": "Charlie", "grade": 10, "age": 15}

]

course_documents = [
    {"title": "Mathematics", "teacher": "Ms. Johnson", "room": "Room 101"},
    {"title": "Science", "teacher": "Mr. Anderson", "room": "Room 102"},
    {"title": "History", "teacher": "Mr. Martinez", "room": "Room 103"}
]

result_students = students_collections.insert_many(student_documents)
result_courses = courses_collections.insert_many(course_documents)


print(result_students)
print(result_courses)

