import pymongo
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client["students_2"]
students_collection = db['students']

def insert_student(name, age, roll_no, sub):
    student_data = {
        'name' : name,
        'age' : age,
        "roll_no" : roll_no,
        "sub" : sub
    }

    result = students_collection.insert_one(student_data)
    print(f"Insert Student id: {result}")

insert_student("manik", 21, 1, "Math")
insert_student("john", 22, 2, "History")
insert_student("alice", 20, 3, "Science")
insert_student("manik",21,1,"Math")
all_list = list(students_collection.find({},{"_id":0}))
for student in all_list:
    print(student)