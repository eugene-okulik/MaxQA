# Библиотека

class Book:
    page_material = 'paper'
    has_text = True

    def __init__(self, book_name, author, pages, ISBN, reserve):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.ISBN = ISBN
        self.reserve = reserve

    def print_details_book(self):
        if self.reserve:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages}, '
                f'материал: {self.page_material}, зарезервирована')
        else:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages}, '
                f'материал: {self.page_material}')


class SchoolBook(Book):
    def __init__(self, book_name, author, pages, ISBN, reserve, subject, school_class, tasks):
        super().__init__(book_name, author, pages, ISBN, reserve)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def print_details_book(self):
        if self.reserve:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages}, '
                f'предмет: {self.subject}, класс: {self.school_class}, зарезервирована')
        else:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, страниц: {self.pages}, '
                f'предмет: {self.subject}, класс: {self.school_class}')


book_1 = Book('name1', 'author1', 100, 'ISBN1', False)
book_2 = Book('name2', 'author2', 200, 'ISBN2', False)
book_3 = Book('name3', 'author3', 300, 'ISBN3', False)
book_4 = Book('name4', 'author4', 400, 'ISBN4', False)
book_5 = Book('name5', 'author5', 500, 'ISBN5', False)

book_1.reserve = True

book_1.print_details_book()
book_2.print_details_book()
book_3.print_details_book()
book_4.print_details_book()
book_5.print_details_book()

school_book_1 = SchoolBook('name1', 'author1', 100, 'ISBN1', False,
                           'Mathematics', 11, True)

school_book_2 = SchoolBook('name1', 'author1', 200, 'ISBN2', False, 'History',
                           8, True)

school_book_3 = SchoolBook('name1', 'author1', 300, 'ISBN3', False, 'Physics',
                           5, True)

school_book_1.reserve = True

school_book_1.print_details_book()
school_book_2.print_details_book()
school_book_3.print_details_book()
