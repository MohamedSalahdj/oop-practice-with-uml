import weakref


class Book():
    num_of_book = 0
    book_borrowed = 0
    
    instances = []
    def __init__(self, id, title, author, total_number_of_copies):
        self.__id = id
        self.__title = title
        self.author = author
        self.__total_number_of_copies = total_number_of_copies
        Book.num_of_book += 1
        self.__class__.instances.append(weakref.proxy(self))

    @property
    def get_id(self):
        return self.__id
    
    @property
    def get_title(self):
        return self.__title
    
    @property
    def get_total_number_of_copies(self):
        return self.__total_number_of_copies
    
    @classmethod
    def Number_of_copies_borrowed(cls, book):
        if book.__total_number_of_copies < 1:
            return 0
        else:
            book.__total_number_of_copies -= 1
            Book.book_borrowed += 1

    @classmethod
    def Number_of_copies_available(cls, book):
        book.__total_number_of_copies += 1
        Book.book_borrowed -= 1

    @property
    def get_all_info_about_book(self):
        if self.__total_number_of_copies > 1:
            return f"Book Name: {self.__title}\nBook ID: {self.__id}\nAuthor name: {self.author.get_full_name}\nThere are {self.__total_number_of_copies} Books in our Library system"
        elif self.__total_number_of_copies == 1:
            return f"Book Name: {self.__title}\nBook ID: {self.__id}\nAuthor name: {self.author.get_full_name}\nThere is {self.__total_number_of_copies} Book in our Library system"