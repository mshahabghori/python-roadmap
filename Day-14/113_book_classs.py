class Book:
    pass


book_01 = Book()
book_01.title = "Harry Potter"
book_01.author = "J.K Rowling"
book_01.price = 500

book_02 = Book()
book_02.title = "Atomic Habits"
book_02.author = "James Clear"
book_02.price = 400

book_03 = Book()
book_03.title = "Python Basics"
book_03.author = "John Smith"
book_03.price = 600


books = [book_01, book_02, book_03]


while True:

    choice = input("Enter book name to search: ").lower()

    found = False

    for book in books:
        if book.title.lower() == choice:
            print("\nBook Found")
            print("Title =", book.title)
            print("Author =", book.author)
            print("Price =", book.price)
            found = True
            break

    if found == False:
        print("Book not Found")

    while True:
        again = input("\nDo you want to search another book? ").lower()

        if again == "no":
            exit()

        elif again == "yes":
            break

        else:
            print("Invalid Input")
