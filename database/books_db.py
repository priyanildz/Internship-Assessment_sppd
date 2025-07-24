from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["library"]  # Database name
collection = db["books"]  # Collection name

books = [
    {"title": "AI for Beginners", "author": "John Doe", "ISBN": "123-A", "year": 2020},
    {"title": "Deep Learning", "author": "Jane Smith", "ISBN": "456-B", "year": 2022},
    {"title": "Machine Learning Guide", "author": "John Doe", "ISBN": "789-C", "year": 2021},
    {"title": "MongoDB Essentials", "author": "Alice Ray", "ISBN": "101-D", "year": 2023},
]

if collection.count_documents({}) == 0:
    collection.insert_many(books)
    print("Inserted sample data.")

# 1. Find all books by a specific author
author_name = "John Doe"
print(f"\nBooks by {author_name}:")
for book in collection.find({"author": author_name}):
    print(book)

# 2. Find the most recently published book
latest_book = collection.find().sort("year", -1).limit(1)
print("\nMost recently published book:")
for book in latest_book:
    print(book)

# 3. Update the publication year of a book
isbn_to_update = "123-A"
new_year = 2025
update_result = collection.update_one(
    {"ISBN": isbn_to_update},
    {"$set": {"year": new_year}}
)
print(f"\nUpdated {update_result.modified_count} document(s).")