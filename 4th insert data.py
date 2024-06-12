import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017")
database = client["bookstore"]
collection = database["books"]

def insert_book(title, author, publish_year, pages, rating,user_name = None, phone_no = None, email_id = None,pin_code = None):

    user_data = {
        "name": user_name,
        "phone" : phone_no,
        "email" : email_id,
        "pin_code" : pin_code,
        "purchase_date" : datetime.now().strftime('%Y - %m - %d')
    }


    book_data = {
        "title": title,
        "author": author,
        "publish_year": publish_year,
        "pages": pages,
        "rating": rating,
        "user_bought": [user_data]
    }

    result = collection.insert_one(book_data)
    print(f"Book {title} has been inserted in {result.inserted_id} purchased by {user_name} at {datetime.now().strftime('%Y - %m - %d')}")


insert_book("Book Name 1", "Author Name 1", 2001, 301, 8.1,"First User Buy", "+91 1233210000", "1stuser@gmail.com", 7214301)

insert_book("Book Name 2", "Author Name 2", 2002, 302, 8.1,"Secpmd User Buy", "+91 1233210002", "2nduser@gmail.com", 7214302)

insert_book("Book Name 3", "Author Name 3", 2003, 303, 8.1,"Third User Buy", "+91 1233210003", "3rduser@gmail.com", 7214303)

insert_book("Book Name 4", "Author Name 4", 2004, 304, 8.1,"Fourth User Buy", "+91 1233210004", "4thuser@gmail.com", 7214304)

insert_book("Book Name 5", "Author Name 5", 2005, 305, 8.1,"Fifth User Buy", "+91 1233210005", "5thuser@gmail.com", 7214305)
