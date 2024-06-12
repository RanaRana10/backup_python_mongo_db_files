from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['user_database']

user_data = {
    'userid': 123,
    'username': '@username',
    'first_name': 'John',
    'last_name': 'Doe',
    'full_name': 'John Doe',
    'referred_by': 'Referrer',
    'referred_to': 'Referee',
    'first_start': '2024-02-19',
    'plan': 'Gold',
    'purchase_date': '2024-02-19',
    'image_quota': 100,
    'images_processed': 10,
    'other_record': 'Other record',
    'phone_numbers': ['1234567890', '9876543210'],
    'email_addresses': ['john@example.com', 'john.doe@example.com']
}

# Insert user data into MongoDB
user_collection = db['users']
user_collection.insert_one(user_data)

# Query user data
user = user_collection.find_one({'userid': 123})
print(user)
