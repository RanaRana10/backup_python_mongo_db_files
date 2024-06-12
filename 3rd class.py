import pymongo
from datetime import datetime

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["students_2"]
students_collection = db['students']

# Create a unique index on the "roll_no" field
students_collection.create_index([('roll_no', pymongo.ASCENDING)], unique=True)

def get_latest_roll_number():
    # Find the document with the highest roll number
    latest_student = students_collection.find_one(sort=[('roll_no', pymongo.DESCENDING)])
    if latest_student:
        return latest_student['roll_no']
    else:
        return 0  # Return 0 if no records are found

def insert_student(name, age, sub):
    latest_roll_number = get_latest_roll_number()
    new_roll_number = latest_roll_number + 1

    student_data = {
        'name': name,
        'age': age,
        'roll_no': new_roll_number,
        'sub': sub,
    }

    try:
        result = students_collection.insert_one(student_data)
        print(f"Insert Student id: {result.inserted_id}, Roll Number: {new_roll_number}")
    except pymongo.errors.DuplicateKeyError:
        print(f"Error: Duplicate roll number. Student not inserted.")

# Insert student records
insert_student("manik", 21, "Math")
insert_student("john", 22, "History")
insert_student("alice", 20, "Science")
insert_student("bob", 23, "Physics")

# Print all student records
all_list = list(students_collection.find({}, {"_id": 0}))
for student in all_list:
    print(student)
