from person import Author,User
from book import Book
from address import Address

sepqrator = '-'*45

# create object from class Author  
author1 = Author("Mohamed", "Tarek", '123456')

# create objects from class Book  
book1 = Book(9687, 'Paris does not know love', author1, 2)
book2 = Book(1007, 'Misery will never end', author1, 5)


# create address object from Class Adresses
address1 = Address('Desouk', 'Kafr El-sheikh', 'Egypt')

# create user_object from Class User
user1 = User("Mohamed", "Salah", '01113283302', address1, 2018)



# user borrow book from library
user1.borrow_book(book1)
user1.borrow_book(book1)
user1.borrow_book(book2)

# user1.borrow_book(book1)
print(sepqrator)

print(Book.book_borrowed)

print(sepqrator)

# user return book to library
user1.reurn_book(book2)
print(Book.book_borrowed)

# Number of copies available of book
print(book1.get_total_number_of_copies)

# user want to brorrow book from library but this book don't avaiable any book
user1.borrow_book(book1)


print(sepqrator)
book3 ={
    'id':123456,
    'title':"All roads do not lead to Rome",
    'author':author1,
    'total_number_of_copies': 25
}
book3 = user1.Add_book_to_system(**book3)

print(Book.num_of_book)

print(book3.get_title)
print(sepqrator)


#  Search for a book
user1.search_for_book()


