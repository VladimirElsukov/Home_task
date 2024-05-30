# Задание 1
# Реализуйте класс «Студент». Необходимо хранить в полях класса: ФИО,
# дату рождения, название группы, средний балл, предметы. Реализуйте
# конструктор по умолчанию и метод для вывода данных объекта. Реализуйте
# методы валидации данных для атрибутов объекта. Реализуйте доступ к
# отдельным атрибутам класса через методы (геттеры и сеттеры), используя
# декоратор @property и @атрибут.setter.

# from datetime import datetime
# import re
#
# class Student:
#     def __init__(self, full_name="", birth_data=None, group_name="", average_score=0.0, items=""):
#         self.__full_name = full_name
#         self.__birth_data = birth_data
#         self.__group_name = group_name
#         self.__average_score = average_score
#         self.__items = items
#
#     @property
#     def full_name(self):
#         return self.__full_name
#
#     @full_name.setter
#     def full_name(self, value):
#         self.__full_name = self.validate_full_name(value)
#
#     @property
#     def birth_data(self):
#         return self.__birth_data
#
#     @birth_data.setter
#     def birth_data(self, value):
#         self.__birth_data = self.validate_birth_data(value)
#
#     @property
#     def group_name(self):
#         return self.__group_name
#
#     @group_name.setter
#     def group_name(self, value):
#         self.__group_name = self.validate_group_name(value)
#
#     @property
#     def average_score(self):
#         return self.__average_score
#
#     @average_score.setter
#     def average_score(self, value):
#         self.__average_score = self.validate_average_score(value)
#
#     @property
#     def items(self):
#         return self.__items
#
#     @items.setter
#     def items(self, value):
#         self.__items = self.validate_items(value)
#
#     def validate_full_name(self, full_name):
#         letter_pattern = r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$'
#         if re.match(letter_pattern, full_name) and len(full_name) > 6 and len(full_name) < 70:
#             return full_name
#         else:
#             print("Некорректный формат ФИО. Пожалуйста, введите ФИО в формате 'Иванов Иван Иванович'.")
#             return
#
#     def set_full_name(self, full_name=input("Введите ваше ФИО: ")):
#         while True:
#             validated_name = self.validate_full_name(full_name)
#             if validated_name:
#                 self.__full_name = validated_name
#                 return self.__full_name
#             else:
#                 full_name = input("Введите ваше ФИО: ")
#
#     def validate_birth_data(self, birth_data):
#         try:
#             datetime.strptime(birth_data, '%d-%m-%Y')
#             return birth_data
#         except ValueError:
#             print("Некорректный формат даты рождения. Пожалуйста, введите дату в формате 'дд-мм-гггг'.")
#             return
#
#     def set_birth_data(self, birth_data=input("Введите дату рождения (дд-мм-гггг): ")):
#         while True:
#             validated_birth_data = self.validate_birth_data(birth_data)
#             if validated_birth_data:
#                 self.__birth_data = validated_birth_data
#                 return self.__birth_data
#             else:
#                 birth_data = input("Введите дату рождения (дд-мм-гггг): ")
#
#     def validate_group_name(self, group_name):
#         if len(group_name) > 0 and len(group_name) < 50:
#             return group_name
#         else:
#             print("Некорректное название группы. Пожалуйста, введите название группы длиной до 50 символов.")
#             return
#
#     def set_group_name(self, group_name=input("Введите название группы: ")):
#         while True:
#             validated_group_name = self.validate_group_name(group_name)
#             if validated_group_name:
#                 self.__group_name = validated_group_name
#                 return self.__group_name
#             else:
#                 group_name = input("Введите название группы: ")

#     def validate_average_score(self, average_score):
#         if 0.0 <= average_score <= 5.0:
#             return average_score
#         else:
#             print("Некорректный средний балл. Пожалуйста, введите значение от 0.0 до 5.0.")
#             return
#
#     def set_average_score(self, average_score=float(input("Введите средний балл: "))):
#         while True:
#             validated_average_score = self.validate_average_score(average_score)
#             if validated_average_score:
#                 self.__average_score = validated_average_score
#                 return self.__average_score
#             else:
#                 average_score = float(input("Введите средний балл: "))
#
#     def validate_items(self, items):
#         if len(items) > 0 and len(items) < 50:
#             return items
#         else:
#             print("Некорректное название редмета. Пожалуйста, введите название предмета длиной до 50 символов.")
#             return
#
#     def set_items(self, items=input("Введите название предмета: ")):
#         while True:
#             validated_items = self.validate_items(items)
#             if validated_items:
#                 self.__items = validated_items
#                 return self.__items
#             else:
#                 group_name = input("Введите название предмета: ")
#
#
# student = Student()
# student.set_full_name()
# student.set_birth_data()
# student.set_group_name()
# student.set_average_score()
# student.set_items()
#
# print("Ф.И.О студента:", student.full_name)
# print("Дата рождения студента:", student.birth_data)
# print("Название группы:", student.group_name)
# print("Средний балл:", student.average_score)
# print("Название предмета:", student.items)


"""
from datetime import datetime
import re

class Student:
    def __init__(self, full_name="", birth_data=None, group_name="", average_score=0.0, items=""):
        self.__full_name = full_name
        self.__birth_data = birth_data
        self.__group_name = group_name
        self.__average_score = average_score
        self.__items = items

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = self.validate_full_name(value)

    @property
    def birth_data(self):
        return self.__birth_data

    @birth_data.setter
    def birth_data(self, value):
        self.__birth_data = self.validate_birth_data(value)

    @property
    def group_name(self):
        return self.__group_name

    @group_name.setter
    def group_name(self, value):
        self.__group_name = self.validate_group_name(value)

    @property
    def average_score(self):
        return self.__average_score

    @average_score.setter
    def average_score(self, value):
        self.__average_score = self.validate_average_score(value)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = self.validate_items(value)

    def validate_full_name(self, full_name):
        letter_pattern = r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$'
        if re.match(letter_pattern, full_name) and len(full_name) > 6 and len(full_name) < 70:
            return full_name
        else:
            print("Некорректный формат ФИО. Пожалуйста, введите ФИО в формате 'Иванов Иван Иванович'.")
            return

    def set_full_name(self, full_name=input("Введите ваше ФИО: ")):
        while True:
            validated_name = self.validate_full_name(full_name)
            if validated_name:
                self.__full_name = validated_name
                return self.__full_name
            else:
                full_name = input("Введите ваше ФИО: ")

    def validate_birth_data(self, birth_data):
        try:
            datetime.strptime(birth_data, '%d-%m-%Y')
            return birth_data
        except ValueError:
            print("Некорректный формат даты рождения. Пожалуйста, введите дату в формате 'дд-мм-гггг'.")
            return

    def set_birth_data(self, birth_data=input("Введите дату рождения (дд-мм-гггг): ")):
        while True:
            validated_birth_data = self.validate_birth_data(birth_data)
            if validated_birth_data:
                self.__birth_data = validated_birth_data
                return self.__birth_data
            else:
                birth_data = input("Введите дату рождения (дд-мм-гггг): ")

    def validate_group_name(self, group_name):
        if len(group_name) > 0 and len(group_name) < 50:
            return group_name
        else:
            print("Некорректное название группы. Пожалуйста, введите название группы длиной до 50 символов.")
            return

    def set_group_name(self, group_name=input("Введите название группы: ")):
        while True:
            validated_group_name = self.validate_group_name(group_name)
            if validated_group_name:
                self.__group_name = validated_group_name
                return self.__group_name
            else:
                group_name = input("Введите название группы: ")
    def validate_average_score(self, average_score):
        if 0.0 <= average_score <= 5.0:
            return average_score
        else:
            print("Некорректный средний балл. Пожалуйста, введите значение от 0.0 до 5.0.")
            return

    def set_average_score(self, average_score=float(input("Введите средний балл: "))):
        while True:
            validated_average_score = self.validate_average_score(average_score)
            if validated_average_score:
                self.__average_score = validated_average_score
                return self.__average_score
            else:
                average_score = float(input("Введите средний балл: "))

    def validate_items(self, items):
        if len(items) > 0 and len(items) < 50:
            return items
        else:
            print("Некорректное название редмета. Пожалуйста, введите название предмета длиной до 50 символов.")
            return

    def set_items(self, items=input("Введите название предмета: ")):
        while True:
            validated_items = self.validate_items(items)
            if validated_items:
                self.__items = validated_items
                return self.__items
            else:
                group_name = input("Введите название предмета: ")


student = Student()
student.set_full_name()
student.set_birth_data()
student.set_group_name()
student.set_average_score()
student.set_items()

print("Ф.И.О студента:", student.full_name)
print("Дата рождения студента:", student.birth_data)
print("Название группы:", student.group_name)
print("Средний балл:", student.average_score)
print("Название предмета:", student.items)
"""


# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название
# книги, год выпуска, издателя, жанр, автора, цену. Реализуйте конструктор по
# умолчанию и метод для вывода данных объекта. Реализуйте методы
# валидации данных для атрибутов объекта. Реализуйте доступ к отдельным
# атрибутам класса через методы (геттеры и сеттеры), используя декоратор
# @property и @атрибут.setter.


import re
class Book:
    def __init__(self, book_title="", year_release=int, publisher="", genre="", author="", price=int):
        self.__book_title = book_title
        self.__year_release = year_release
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    @property
    def book_title(self):
        return self.__book_title

    @book_title.setter
    def book_title(self, value):
        self.__book_title = self.validate_book_title(value)


    @property
    def year_release(self):
        return self.__year_release

    @year_release.setter
    def year_release(self, value):
        self.__year_release = self.validate_year_release(value)

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, value):
        self.__publisher = self.validate_publisher(value)

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, value):
        self.__genre = self.validate_genre(value)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = self.validate_author(value)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = self.validate_price(value)


    def validate_book_title(self, book_title):
        if re.match(r"^[A-ZА-ЯЁІЇҐ][a-zа-яёіїґ0-9\s-]*$", book_title) and len(book_title) > 0 and len(book_title) < 100:
            return book_title
        else:
            print("Некорректное название книги. Введите название книги длиной до 100 символов с заглавной буквы.")
            return

    def set_book_title(self, book_title=input("Введите название книги: ")):

        while True:
            validated_book_title = self.validate_book_title(book_title)
            if validated_book_title:
                self.__book_title = validated_book_title
                return self.__book_title
            else:
                book_title = input("Введите название книги: ")


    def validate_year_release(self, year_release):
        try:
            year_release = int(year_release)
            if year_release > 0:
                return year_release
            else:
                print("Некорректный год выпуска книги, введите положительное значение.")
                return None
        except ValueError:
            print("Некорректный формат года выпуска. Пожалуйста, введите целое число.")
            return None

    def set_year_release(self, year_release=input("Введите год выпуска книги: ")):

        while True:
            validated_year_release = self.validate_year_release(year_release)
            if validated_year_release is not None:
                self.__year_release = validated_year_release
                return self.__year_release
            else:
                year_release = input("Введите год выпуска книги: ")


    def validate_publisher(self, publisher):
        if re.match(r"^[A-ZА-ЯЁІЇҐ][a-zа-яёіїґ0-9\s-]*$", publisher) and len(publisher) > 0 and len(publisher)<100:
            return publisher
        else:
            print("Некорректное название издателя, введите название длиной до 100 символов с заглавной буквы.")
            return

    def set_publisher(self, publisher=input("Введите название издателя книги: ")):
        while True:
            validate_publisher = self.validate_publisher(publisher)
            if validate_publisher:
                self.__publisher = validate_publisher
                return self.__publisher
            else:
                publisher = input("Введите название издателя книги: ")



    def validate_genre(self, genre):
        if re.match(r"^[A-ZА-ЯЁІЇҐ][a-zа-яёіїґ0-9\s-]*$", genre) and len(genre) > 0 and len(genre) < 100:
            return genre
        else:
            print("Некорректное название жанра книги, введите название длиной до 100 символов с заглавной буквы.")
            return
    def set_genre(self, genre=input("Введите название жанра книги: ")):

        while True:
            validated_genre = self.validate_genre(genre)
            if validated_genre:
                self.__genre = validated_genre
                return self.__genre
            else:
                genre = input("Введите название жанра книги: ")


    def validate_author(self, author ):
        if re.match(r"^[A-ZА-ЯЁІЇҐ][a-zа-яёіїґ0-9\s-]*$", author) and len(author) > 0 and len(author) < 100:
            return author
        else:
            print("Некорректное название автора книги, введите название длиной до 100 символов с заглавной буквы.")
            return

    def set_author(self, author=input("Введите автора книги: ")):

        while True:
            validated_author = self.validate_genre(author)
            if validated_author:
                self.__author = validated_author
                return self.__author
            else:
                author = input("Введите автора книги: ")

    def validate_price(self, price):
        try:
            price = float(price)
            if price >= 0:
                return price
            else:
                print("Цена не может быть отрицательной, введите неотрицательное значение для цены.")
                return None
        except ValueError:
            print("Некорректный формат цены. Пожалуйста, введите числовое значение.")
            return None

    def set_price(self, price=input("Введите цену книги: ")):

        while True:
            validated_price = self.validate_price(price)
            if validated_price is not None:
                self.__price = validated_price
                return self.__price
            else:
                price = input("Введите цену книги: ")

book = Book()
book.set_book_title()
book.set_year_release()
book.set_publisher()
book.set_genre()
book.set_author()
book.set_price()
print("Название книги:", book.book_title)
print("Год выпуска книги:", book.year_release)
print("Издатель книги:", book.publisher)
print("Жанр книги:", book.genre)
print("Автор книги", book.author)
print("Цена книги:", book.price)




