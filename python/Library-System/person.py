from book import Book


class Person():
    def __init__(self, fname, lname, phone):
        self.__fname = fname
        self.__lname = lname
        self.__phone = phone
    
    @property
    def get_full_name(self):
        return self.__fname+" "+self.__lname
    
    @property
    def get_phone_number(self):
        return self.__phone


class User(Person):
    def __init__(self, fname, lname, phone, address, id):
        super().__init__(fname, lname, phone)
        self.address = address
        self.__id = id
    
    @property
    def get_address(self):
        return f"Address: {self.address.get_city}\{self.address.get_state}\{self.address.get_country}"
    
    def borrow_book(self, book):
        if Book.Number_of_copies_borrowed(book) !=0:
            print(f"Wow you can borrow '{book.get_title}'")
        else:
            print(f"Now we don't have copies from '{book.get_title}'")

    def reurn_book(self, book):
        Book.Number_of_copies_available(book)
        print("Return a book was completed")
    
    def Add_book_to_system(self, **book):
       return Book(book['id'], book['title'], book['author'], book['total_number_of_copies'])
    
    def remove_book(self, book):
        del book.author
        del book._Book__title
        del book._Book__id
        del book._Book__total_number_of_copies
        Book.num_of_book -=1
        print("Completed Delete")

    def search_for_book(self):
        book_id = int(input("Enter id for Book: "))
        for instance in Book.instances:
            # print(instance.get_id)
            if instance.get_id == book_id:
                print(instance.get_all_info_about_book)


class Author(Person):
    def __init__(self, fname, lname, phone):
        super().__init__(fname, lname, phone)
