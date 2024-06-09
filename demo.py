available_books = {"001": {
        "title": "Madol Duwa",
        "author": "martin",
        "availability status": "True"
    },
    "002": {
        "title": "Aba yaluwo",
        "author": "martin",
        "availability status": "True"
    }
}

def display_available_books():
    for id, books in available_books.items():
        print(id, books)
def borrow_a_book():
    what_book = input("Enter you want book ID: ")
    if what_book in available_books and available_books[what_book]["availability status"] == "True":
        print("Book is Available, Can Borrow!")
        available_books[what_book]["availability status"] = "False"
        display_available_books()
    else:
        print("Book is Unavailable!")
        display_available_books()

def return_a_book():
    what_book = input("Enter your return book ID: ")
    if available_books[what_book]["availability status"] == "False":
        print("Book will return.")
        available_books[what_book]["availability status"] = "True"
        display_available_books()
    else:
        print("Book is already returned.")

def add_a_book():
    new_book_id = input("Enter new book ID: ")
    title = input("Enter book title: ")
    author = input("Enter author: ")

    if new_book_id not in available_books:
        available_books[new_book_id] = {}

    available_books[new_book_id]["title"] = title
    available_books[new_book_id]["author"] = author
    available_books[new_book_id]["availability status"] = True

    display_available_books()


while True:
    print("Enter your choice.")

    print("1.Display available books")
    print("2.Borrow a book")
    print("3.Return a book")
    print("4.Add a book")
    print("5.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_available_books()
    elif choice == "2":
        borrow_a_book()
    elif choice == "3":
        return_a_book()
    elif choice == "4":
        add_a_book()
    elif choice == "5":
        get_exit_confirm = input("Are you sure to exit, y/n: ")
        if get_exit_confirm == "y":
            exit()
        else:
            continue




