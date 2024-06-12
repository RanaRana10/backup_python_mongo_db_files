from pymongo import MongoClient

# Connect to the local MongoDB server
client = MongoClient('mongodb://localhost:27017/')

# Access a database (create one if it doesn't exist)
db = client['school_database']

# Access a collection for student records (create one if it doesn't exist)
students_collection = db['students']

# Insert sample student records
student_data_1 = {
    'name': 'John Doe',
    'age': 20,
    'roll_number': 'S123456',
    'subjects': ['Math', 'Science', 'History']
}

student_data_2 = {
    'name': 'Jane Smith',
    'age': 19,
    'roll_number': 'S123457',
    'subjects': ['English', 'Physics', 'Computer Science']
}

# Insert the documents into the collection
result_1 = students_collection.insert_one(student_data_1)
result_2 = students_collection.insert_one(student_data_2)

# Print the inserted documents' IDs
print(f"Inserted student record 1 with ID: {result_1.inserted_id}")
print(f"Inserted student record 2 with ID: {result_2.inserted_id}")

# Query and print all student records
all_students = students_collection.find({}, {"_id":0, "name" :1 })

# Print each student record
for student in all_students:
    print(student)
