print("ONline Library Management")

book_name=["Python","Java","C++"]
issued_books=[]
members=["Anju","Manju","Chinju"]
print("Available books: ",book_name)
print("Issued books: ",issued_books)
print("Members: ",members)

print(book_name[0])
print(book_name[1])
print(book_name[2])
print(book_name[0:2])

print("[python,java,c++]".upper())
print("[python,java,c++]".lower())
print("[python,java,c++]".title())

issued_books.append("HTML")
print(issued_books)
book_name.insert(0,"Rust")
print(book_name)
book_name.remove("C++")
print(book_name)
members.pop(1)
print(members)
book_name.sort()
print(book_name)
book_name.reverse()
print(book_name)

available_books = [book for book in book_name]
print("Available Books: ",available_books)
p_books=[book for book in book_name if book.startswith("P")]
print("Books starting with P: ",p_books)
uppercase_books=[book.upper() for book in book_name]
print("Uppercase Book Names: ",uppercase_books)

categories = ("Programming","Database","Networking")
print("Book Categories:")
cat1,cat2,cat3=categories
print(cat1)
print(cat2)
print(cat3)

genres={"Python","Java","C++"}
print("Unique Genres:",genres)
genres.add("Database")
genres.remove("Java")
print("Updated Genres:",genres)

genres1={"Python","Java","C++"}
genres2={"Python","Database","C++"}
print("Union:",genres1.union(genres2))
print("Intersection:",genres1.intersection(genres2))

book = {
    "book_id":200,
    "title":"Python Basics",
    "author":"Anju",
    "status":"available"
}

print("Book Details: ",book)
print("Book title: ",book["title"])
print("Dictionary Keys: ",book.keys())
print("Dictionary Values: ",book.values())
print("Dictionary Items: ",book.items())
print("Book Author: ",book.get("author"))

book.update({"title": "Python Programming"})

print("Updated Book: ",book)
book.pop("author")
print("After removing author: ",book)

member={
    "name":"Anju",
    "member_id":200,
    "age":21
}
print("Member Details: ",member)
print("Member name: ",member["name"])

issue_status={
    "Python":"Issued",
    "Java":"Available",
    "C++":"Available"
}
print("Issue Status:",issue_status)

library={
    200:{
        "title":"Python",
        "author":"Anju",
        "status":"Available"
    },
    201:{
        "title":"Java",
        "author":"Chinju",
        "status":"Issued"
    }
}
print("Nested Dictionary Data:",library)
print("First Book:",library[200])
print("First Book Title:",library[200]["title"])

student={
    "name":"Chinju",
    200:"Python",
    (1,2):"Programming"
}
print("Immutable Keys Dictionary: ",student) 