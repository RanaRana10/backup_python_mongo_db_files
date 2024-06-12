import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")

database = client["bookstore"]
collection = database["books"]

def find_all_books():
    cursor = collection.find()

    for document in cursor:
        print(document)

if __name__ == "__main__":
    find_all_books()