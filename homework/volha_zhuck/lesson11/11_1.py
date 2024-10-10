from abc import abstractmethod


class Book:
    material_pages = "бумага"
    text = False
    book_name = ''
    author = ''
    pages = 0
    ISBN = ''
    reserv = False

    def __init__(self, material_pages, text, book_name, author, pages, reserv=False) -> None:
        self.material_pages = material_pages
        self.text = text
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.reserv = reserv
        pass

    @abstractmethod
    def printBook(self):
        if self.reserv:
            print(
                f"Название: {self.book_name}, Автор: {self.author}, "
                f"страниц: {self.pages}, материал: {self.material_pages}, "
                "зерезервирована"
        )
        else:
            print(
                f"Название: {self.book_name}, Автор: {self.author}, "
                f"страниц: {self.pages}, материал: {self.material_pages}"
        )


class SchoolBooks(Book):
    lesson = ''
    grade = ''
    practice = True

    def __init__(self, material_pages, text, book_name, author, pages, lesson, grade, practice, reserv=False) -> None:
        super().__init__(material_pages, text, book_name, author, pages, reserv)
        self.lesson = lesson
        self.grade = grade
        self.practice = practice

    def printBook(self):
        if self.reserv:
            print(
                f"Название: {self.book_name}, Автор: {self.author}, "
                f"страниц: {self.pages}, предмет: {self.lesson}, класс: {self.grade}, "
                "зерезервирована"
        )
        else:
            print(
                f"Название: {self.book_name}, Автор: {self.author}, "
                f"страниц: {self.pages}, предмет: {self.lesson}, класс: {self.grade}"
        )


book1 = Book('бумага', True, 'Идиот', 'Достоевский', 500)
book1.printBook()
book2 = Book('бумага', True, 'Преступление и наказание', 'Достоевский', 300, True)
book2.printBook()
book3 = Book('глянец', True, 'Мертывые души', 'Чехов', 450)
book3.printBook()
book4 = Book('папирус', True, 'Книга мертвых', 'Неизвестен', 50)
book4.printBook()
book5 = Book('бумага', True, 'Война и мир', 'Толстой', 1000)
book5.printBook()
book6 = SchoolBooks('бумага', True, 'Алгебра', 'Иванов', 666, 'Математика', '2', True, True)
book6.printBook()
book7 = SchoolBooks('бумага', True, 'История', 'Петров', 200, 'История', '6', True)
book7.printBook()
book8 = SchoolBooks('бумага', True, 'География', 'Сидоров', 150, 'География', '8', True, True)
book8.printBook()
