books = input().split("&")

tokens = input()
while not tokens == "Done":
    tokens = tokens.split(" | ")
    command = tokens[0]

    if command == "Add Book":
        book = tokens[1]
        if book not in books:
            books.insert(0, book)

    elif command == "Take Book":
        book = tokens[1]
        if book in books:
            books.remove(book)

    elif command == "Swap Books":
        book_one = tokens[1]
        book_two = tokens[2]
        if book_one in books and book_two in books:
            books_one_index = books.index(book_one)
            book_two_index = books.index(book_two)
            books[books_one_index], books[book_two_index] = books[book_two_index], books[books_one_index]

    elif command == "Insert Book":
        book = tokens[1]
        books.append(book)

    elif command == "Check Book":
        index = int(tokens[1])
        if 0 <= index < len(books):
            print(books[index])

    tokens = input()

print(", ".join(books))