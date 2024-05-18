# Задание 1
# Реализуйте класс «Студент». Необходимо хранить в полях класса: ФИО,
# дату рождения, название группы, средний балл, предметы. Реализуйте
# конструктор по умолчанию и метод для вывода данных объекта. Реализуйте
# методы валидации данных для атрибутов объекта. Реализуйте доступ к
# отдельным атрибутам класса через методы (геттеры и сеттеры), используя
# декоратор @property и @атрибут.setter.

from datetime import datetime
import re

class Student:
    def __init__(self, full_name="", birth_data=None, group_name="", average_score=0.0, items=""):
        self.__full_name = full_name
        self.__birth_data = birth_data
        self.__group_name = group_name
        self.__average_score = average_score
        self.__items = items

    def validate_full_name(self, full_name):
        letter_pattern = r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$'
        if re.match(letter_pattern, full_name) and len(full_name) > 6 and len(full_name) < 60:
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
        ...
    def validate_group_name(self, group_name):
        ...
    def validate_average_score(self, average_score):
        ...

    def validate_items(self, items):
        ...



student = Student()
student.set_full_name()
print("Введенное ФИО:", student._Student__full_name)




# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название
# книги, год выпуска, издателя, жанр, автора, цену. Реализуйте конструктор по
# умолчанию и метод для вывода данных объекта. Реализуйте методы
# валидации данных для атрибутов объекта. Реализуйте доступ к отдельным
# атрибутам класса через методы (геттеры и сеттеры), используя декоратор
# @property и @атрибут.setter.