print("ONLINE LIBRARY MANAGEMENT SYSTEM")

books=["Python", "Java", "C++"]
issued_books = ["Java"]
members=["Afla", "Alan", "Afsal"]

print("Available Books:")
print(books)
print("Issued Books:")
print(issued_books)
print("Members:")
print(members)

book_name="Python"
print(book_name[0])
print(book_name[-1])
print(book_name[0:5])
print(members[0])
print(books[0:2])


book_title="python basics"

print(book_title.upper())
print(book_title.lower())
print(book_title.title())

member_name = "Adrian"
new_title = book_title.replace("basics", "programming")
print(new_title)
words = book_title.split()
print(words)

text="Python"

books.append("HTML")
books.insert(1, "SQL")
print("After adding books:")
print(books)
books.remove("C++")
print("After removing C++:")
print(books)
books.pop()
print("After pop:")
print(books)
books.sort()
print("Sorted ooks:")
print(books)
books.reverse()
print("Reversed books:")
print(books)

uppercase_books=[book.upper() for book in books]

print("Uppercase Book Names:")
print(uppercase_books)
p_books = [book for book in books if book.startswith("P")]
print("Books starting with P:")
print(p_books)

categories = ("Programming","Database","Networking")
print("Book Categories:")

cat1, cat2, cat3 = categories
print(cat1)
print(cat2)
print(cat3)

genres={"Python","Java","Python","C++"}
print("Unique Genres:")
print(genres)
genres.add("Database")
genres.remove("Java")
print("Updated Genres:")
print(genres)

genres1={"Python", "Java", "C++"}
genres2={"Python", "Database", "C++"}

print("Union:")
print(genres1.union(genres2))

print("Intersection:")
print(genres1.intersection(genres2))

book = {
    "book_id": 101,
    "title": "Python Basics",
    "author": "Alex"
}

print("Book Details:")
print(book)
print("Book title:")
print(book["title"])
print("Dictionary Keys:")
print(book.keys())
print("Dictionary Values:")
print(book.values())
print("Dictionary Items:")
print(book.items())
print("Book Author:")
print(book.get("author"))

book.update({"title": "Python Programming"})

print("Updated Book:")
print(book)
book.pop("author")

print("After removing author:")
print(book)

library = {
    101: {"title": "Python", "author": "Alex"},
    102: {"title": "Java", "author": "David"}
}

print("Nested Dictionary Data:")
print(library)
print("First Book:")
print(library[101])
print("First Book Title:")
print(library[101]["title"])
student = {
    "name": "Afla",
    101: "Python",
    (1, 2): "Programming"
}

print("Immutable Keys Dictionary:")
print(student)

print("Hash Value:")
print(hash("Python"))


# None and NoneType

book_issued = None
member_fine = None

print("Book Not Issued:")
print(book_issued)

print("Member Fine:")
print(member_fine)

print("Type of None:")
print(type(None))