class LibraryBook:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False
        
# Клас LibraryBookDetails містить методи для перевірки стану книги (check_condition) 
# та отримання інформації про книгу (get_book_info)
class LibraryBookDetails:
    def __init__(self, book):
        self.book = book

    def check_condition(self):
        # Припустимо, що стан книги можна перевірити таким чином
        # Для прикладу повернемо рядок "Good"
        return "Good"

    def get_book_info(self):
        return f"Title: {self.book.title}, Author: {self.book.author}, Publication Year: {self.book.publication_year}"

# Клас LibraryBookWithDetails агрегує об'єкт класу LibraryBook і делегує йому базові методи роботи
# з книгою (check_out і return_book).
# Також цей клас використовує об'єкт LibraryBookDetails для додавання додаткової функціональності.
class LibraryBookWithDetails:
    def __init__(self, title, author, publication_year):
        self.library_book = LibraryBook(title, author, publication_year)
        self.details = LibraryBookDetails(self.library_book)

    def check_out(self):
        return self.library_book.check_out()

    def return_book(self):
        return self.library_book.return_book()

    def check_condition(self):
        return self.details.check_condition()

    def get_book_info(self):
        return self.details.get_book_info()

# Використання коду
book = LibraryBookWithDetails("The Great Gatsby", "F. Scott Fitzgerald", 1925)
print(book.check_out())  # True
print(book.check_out())  # False, книга вже видана
print(book.return_book())  # True
print(book.return_book())  # False, книга вже повернена
print(book.check_condition())  # Good
print(book.get_book_info())  # Title: The Great Gatsby, Author: F. Scott Fitzgerald, Publication Year: 1925
