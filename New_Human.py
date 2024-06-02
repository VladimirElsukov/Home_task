'''
Задание 1
Реализуйте класс«Человек».
Необходимо хранить в полях класса: ФИО, возраст, контактный
телефон. Реализуйте конструктор по умолчанию и метод для вывода данных.
Реализуйте доступ к отдельным полям класса через методы класса (геттеры
и сеттеры).
Реализуйте метод класса, который принимает в качестве параметров
ФИО, дату рождения (день, месяц, год), контактный телефон. Создайте
экземпляр класса используя альтернативный конструктор.
Реализуйте статический метод, который вычисляет возраст человека
относительно текущего дня по переданной дате рождения
'''
from datetime import datetime
import re
class Human:
    def __init__(self, full_name: str, birth_date: str, contact_phone: str):
        self.__full_name = full_name
        self.__birth_date = birth_date
        self.__contact_phone = contact_phone


    def data_output(self):
        return (
            f"Ф.И.О.: {self.__full_name}\n"
            f"Дата рождения: {self.__birth_date}\n"
            f"Контактный телефон: {self.__contact_phone}"
        )

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name):
        self.__full_name = self.__validate_string(full_name, 'full_name')

    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, birth_date):
        self.__birth_date = self.__validate_birth_data(birth_date, 'birth_date')

    @property
    def contact_phone(self):
        return self.__contact_phone

    @contact_phone.setter
    def contact_phone(self, contact_phone):
        self.__contact_phone = self.__validate_contact_phone(contact_phone)



    def __validate_string(self, value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{field_name} должен быть строкой")
        if not value:
            raise ValueError(f"{field_name} не может быть пустым")

        valid_characters = set(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ')
        if not all(i in valid_characters for i in value):
            raise ValueError(f"{field_name} должен содержать только символы кириллицы, латиницы или пробелы")

        words = value.split()
        for i, word in enumerate(words):
            if not word.isalpha():
                raise ValueError(f"{field_name} должно содержать только буквы и пробелы")
            words[i] = word.lower().capitalize()
        return ' '.join(words)



    def __validate_birth_data(self, birth_data):
        try:
            validated_birth_data = datetime.strptime(birth_data, '%d-%m-%Y').strftime('%d-%m-%Y')
            return validated_birth_data
        except ValueError:
            birth_data_input = input("Некорректный формат даты рождения. Введите дату рождения (дд-мм-гггг): ")
            print(f"Вы ввели: {birth_data_input}")
            return None


    def __validate_contact_phone(self, contact_phone):
        import re
        pattern = r'^[\+\(]?[1-9]{1,3}[\)\s-]?[\d]{1,14}$'

        if re.match(pattern, contact_phone):
            return contact_phone
        else:
            raise ValueError("Неверный формат номера телефона")

    @staticmethod
    def calculate_age(birth_date):
        today = datetime.today()
        try:
            birthday = datetime.strptime(birth_date, '%d-%m-%Y')
            years = today.year - birthday.year - 1 if (today.month, today.day) < (
            birthday.month, birthday.day) else today.year - birthday.year
            months = 12 - birthday.month + today.month if today.day >= birthday.day else 12 - birthday.month + today.month - 1
            days = today.day + (30 - birthday.day) if today.day < birthday.day else today.day - birthday.day

            return f"Возраст человека: {years} years, {months} months, {days} days"
        except ValueError:
            return None


human = Human("Иванов Иван Иванович", "12-12-1978", "+7(999)680-15-15")
print("\nВывод всей информации:")
print(human.data_output())
print("\nМеняем и выводим Ф.И.О:")
human.full_name = "ветров иван петрович"
print(human.full_name)
print("\nВыводим дату рождения:")
print(human.birth_date)

print("\nВыводим телефон:")
human.contact_phone = "+79809805454"
print(human.contact_phone)


age = Human.calculate_age("02-02-2017")
if age is not None:
    print(age)
else:
    print("Неверный формат данных")

