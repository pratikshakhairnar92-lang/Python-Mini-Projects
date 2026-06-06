from colorama import Fore, Style, init

init()

books = []

while True:

    print(Fore.CYAN + "\n===================================")
    print(Fore.YELLOW + "   LIBRARY MANAGEMENT SYSTEM")
    print(Fore.CYAN + "===================================")

    print(Fore.GREEN + "1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Total Books")
    print("8. Exit")

    choice = input(Fore.MAGENTA + "\nEnter Your Choice: ")

    if choice == "1":

        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "name": book_name,
            "author": author,
            "status": "Available"
        }

        books.append(book)

        print(Fore.GREEN + "\nBook Added Successfully!")

    elif choice == "2":

        if len(books) == 0:
            print(Fore.RED + "\nNo Books Available!")

        else:
            print(Fore.YELLOW + "\n===== BOOK LIST =====")

            for book in books:
                print(Fore.CYAN + "------------------------")
                print("Book ID :", book["id"])
                print("Book Name :", book["name"])
                print("Author :", book["author"])
                print("Status :", book["status"])

    elif choice == "3":

        search = input("Enter Book Name: ")

        found = False

        for book in books:

            if book["name"].lower() == search.lower():

                print(Fore.GREEN + "\nBook Found!")
                print("Book ID :", book["id"])
                print("Author :", book["author"])
                print("Status :", book["status"])

                found = True

        if not found:
            print(Fore.RED + "\nBook Not Found!")

    elif choice == "4":

        issue_book = input("Enter Book Name To Issue: ")

        found = False

        for book in books:

            if book["name"].lower() == issue_book.lower():

                if book["status"] == "Available":

                    book["status"] = "Issued"
                    print(Fore.GREEN + "\nBook Issued Successfully!")

                else:
                    print(Fore.RED + "\nBook Already Issued!")

                found = True

        if not found:
            print(Fore.RED + "\nBook Not Found!")

    elif choice == "5":

        return_book = input("Enter Book Name To Return: ")

        found = False

        for book in books:

            if book["name"].lower() == return_book.lower():

                if book["status"] == "Issued":

                    book["status"] = "Available"
                    print(Fore.GREEN + "\nBook Returned Successfully!")

                else:
                    print(Fore.RED + "\nBook Is Already Available!")

                found = True

        if not found:
            print(Fore.RED + "\nBook Not Found!")

    elif choice == "6":

        delete_book = input("Enter Book Name To Delete: ")

        found = False

        for book in books:

            if book["name"].lower() == delete_book.lower():

                books.remove(book)

                print(Fore.GREEN + "\nBook Deleted Successfully!")

                found = True
                break

        if not found:
            print(Fore.RED + "\nBook Not Found!")

    elif choice == "7":

        print(Fore.YELLOW + "\nTotal Books :", len(books))

    elif choice == "8":

        print(Fore.GREEN + "\nThank You For Using Library Management System!")
        break

    else:

        print(Fore.RED + "\nInvalid Choice!")

    print(Style.RESET_ALL)