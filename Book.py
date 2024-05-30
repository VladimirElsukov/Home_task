'''
Задание 2.
Реализуйте класс «Книга». Необходимо хранить в полях класса:
название книги, год выпуска, издателя, жанр, автора, цену. Реализуйте
конструктор по умолчанию и метод для вывода данных.
'''

class Book:
    def __init__(self, title_book="", year_release=0, publisher="", genre="", author="", price=0):
        self.__title_book = title_book
        self.__year_release = year_release
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def data_output(self):
        print("Название книги:", self.__title_book)
        print("Год выпуска:", int(self.__year_release))
        print("Издатель:", self.__publisher)
        print("Жанр:", self.__genre)
        print("Автор:", self.__author)
        print("Цена:", float(self.__price))

book = Book("Поднятая целина", 1932, "журнал'Новый мир'", "роман", "М.А.Шолохов", 494)
book.data_output()
