class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"\nYou successfully borrowed '{self.title}'.")
        else:
            print(f"\nSorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"\nYou successfully returned '{self.title}'.")
        else:
            print(f"\n'{self.title}' is already available.")

    def is_available(self):
        return self.available

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Status: {status}")
        print("-" * 30)


# Pre-existing books
library = [
    Book("Python Programming", "John Smith", "2020"),
    Book("Data Structures", "Maria Cruz", "2019"),
    Book("Introduction to AI", "David Lee", "2022")
]


# Main Program
print("=== Library Book Management System ===")

while True:
    print("\nMenu:")
    print("1 - Display All Books")
    print("2 - Borrow a Book")
    print("3 - Return a Book")
    print("4 - Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("\n--- Library Books ---")
        for i, book in enumerate(library):
            print(f"\nBook Number: {i + 1}")
            book.display_info()

    elif choice == "2":
        print("\n--- Borrow a Book ---")
        for i, book in enumerate(library):
            print(f"{i + 1} - {book.title}")

        book_choice = input("Enter book number to borrow: ")

        if book_choice.isdigit() and 1 <= int(book_choice) <= len(library):
            library[int(book_choice) - 1].borrow_book()
        else:
            print("Invalid book number.")

    elif choice == "3":
        print("\n--- Return a Book ---")
        for i, book in enumerate(library):
            print(f"{i + 1} - {book.title}")

        book_choice = input("Enter book number to return: ")

        if book_choice.isdigit() and 1 <= int(book_choice) <= len(library):
            library[int(book_choice) - 1].return_book()
        else:
            print("Invalid book number.")

    elif choice == "4":
        print("\nExiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
