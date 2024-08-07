import json
import os

#定义Book类，包括标题、作者、ISBN和可用状态
class Book:
    def __init__(self,title,author,isbn,available=True):
        self.title = title
        self.author = author
        self.isbn  = isbn
        self.available = available
    def __repr__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN:{self.isbn}) - {status}"
#定义Library类，管理图书的添加、查看、借阅和归还，使用JSON文件进行数据持久化。
class Library:
    def __init__(self,filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        if os.path.exists(self.filename):
            with open(self.filename,'r') as file:
                books_data = json.load(file)
                return [Book(**data) for data in books_data]
        return []
    def save_books(self):
        with open(self.filename,'w') as file:
            json.dump([book.__dict__ for book in self.books], file)
    def add_book(self,title,author,isbn):
        new_book = Book(title,author,isbn)
        self.books.append(new_book)
        self.save_books()
        print("Book added successfully")
    def view_books(self):
        if not self.books:
            print("No books available in this library")
        for book in self.books:
            print(book)
    def borrow_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    self.save_books()
                    print(f"You have borrowed {book.title}")
                    return
                else:
                    print("Sorry,this book is already borrowed!")
        print("Book not found")
    def return_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = True
                    self.save_books()
                    print(f"You have returned {book.title}")
                    return
                else:
                    print("Sorry,this book is not borrowed!")
        print("Book not found")
#提供用户交互菜单，调用相应的库函数执行操作
def main():
    library = Library()

    while True:
        print("\n1.Add Book\n2.View Books\n3.Borrow Book\n4.Return Book\n5.Exit")
        choice = input("Choose your option:")
        if choice == "1":
            title = input("Enter book title:")
            author = input("Enter book author:")
            isbn = input("Enter book ISBN:")
            library.add_book(title,author,isbn)
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            isbn = input("Enter book ISBN to borrow")
            library.borrow_book(isbn)
        elif choice == "4":
            isbn = input("Enter ISBN to return")
            library.return_book(isbn)
        elif choice == "5":
            breakpoint()
        else:
            print("Invalid choice!Please try again.")

if __name__ == "__main__":
    main()