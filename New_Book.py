'''
Задание 2
Реализуйте класс«Книга».
Необходимо хранить в полях класса: название, жанр, год публикации.
Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
Реализуйте метод класса, который принимает в качестве параметра
путь к файлу где содержится информация о книге. Создайте экземпляр класса
используя альтернативный конструктор.
Добавьте классу статическую переменную, которая хранит тип
экземпляра книги. По умолчанию все объекты должны создаваться с типом
«Бумажный экземпляр». Реализуйте метод, который изменяет для отдельного
объекта тип на «Электронный экземпляр».
'''
import os
class Book:
    def __init__(self, title_book: str, genre: str, year_release=0):
        self.__title_book = title_book
        self.__genre = genre
        self.__year_release = year_release


    def data_output(self):
        print("Название книги:", self.__title_book)
        print("Жанр:", self.__genre)
        print("Год выпуска:", int(self.__year_release))

    @property
    def title_book(self):
        return self.__title_book

    @title_book.setter
    def title_book(self, title_book):
        self.__title_book = self.__validate_title_book(title_book)

    def __validate_title_book(self, title_book):

        if not isinstance(title_book, str):
            raise TypeError(f"{title_book} должен быть строкой")
        if not title_book:
            raise ValueError(f"{title_book} не может быть пустым")

        valid_characters = set(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ')
        if not all(i in valid_characters for i in title_book):
            raise ValueError(f"{title_book} должен содержать только символы кириллицы, латиницы или пробелы")
        # Сразу приводим все к нижнему регистру и делаем первую букву заглавной.
        return ''.join(title_book.lower().capitalize())

    @staticmethod
    def from_file(file_path):
        if not os.path.exists(file_path):
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("Поднятая целина\nРоман\n1932")

        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines()
            if len(data) != 3:
                raise ValueError("Файл должен содержать заголовок, жанр и год выпуска книги")

            title = data[0]
            genre = data[1]
            year = int(data[2])
            return Book(title, genre, year)



book = Book("Поднятая целина", "Роман", 1932)
book.data_output()
print(book.title_book)
book.title_book = "ЛРДЛ ДОЖДО ЛОЖДО"
print(book.title_book)

book_file = Book.from_file("Put_file.txt")
book_file.data_output()