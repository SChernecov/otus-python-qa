import csv
import json

from test_data.read_write_files.files import BOOKS_FOR_PEOPLE_FILE_R, \
    USERS_FILE, JSON_FILE_FOR_WRITE
from test_data.read_write_files.context_manager import OpenFile

"""Generate dictionary with 'title', 'author', 'pages', 'genre' from rows 
without title from csv file"""
with OpenFile(BOOKS_FOR_PEOPLE_FILE_R, "r") as file:
    reader = csv.reader(file)
    header = next(reader)

    books = []
    for row in reader:
        book = {
            "title": row[0],
            "author": row[1],
            "pages": row[3],
            "genre": row[2]
        }
        books.append(book)

"""Generate dictionary with 'name', 'gender', 'address', 'age' from json file
 and 'books' from csv file with maximally equal rule"""
with OpenFile(USERS_FILE, "r") as file:
    users = json.load(file)

    num_users = len(users)
    num_books = len(books)

    books_per_user = num_books // num_users
    remainder = num_books % num_users

    books_for_persons = []

    for i in range(len(users)):
        user = users[i]
        person = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": []
        }

        if i < remainder:
            for _ in range(i * books_per_user, (i + 1) * books_per_user + 1):
                person["books"].append(books[_])
        else:
            for _ in range(i * books_per_user, (i + 1) * books_per_user):
                person["books"].append(books[_])

        books_for_persons.append(person)

"""Write final json file"""
with OpenFile(JSON_FILE_FOR_WRITE, "w") as file:
    json.dump(books_for_persons, file, indent=4)
