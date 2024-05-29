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



# Задание 2
# Реализуйте класс «Книга». Необходимо хранить в полях класса: название
# книги, год выпуска, издателя, жанр, автора, цену. Реализуйте конструктор по
# умолчанию и метод для вывода данных объекта. Реализуйте методы
# валидации данных для атрибутов объекта. Реализуйте доступ к отдельным
# атрибутам класса через методы (геттеры и сеттеры), используя декоратор
# @property и @атрибут.setter.


