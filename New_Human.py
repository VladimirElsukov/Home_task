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

class Human:
    def __init__(self, full_name="", birth_date="", contact_phone=""):
        self.__full_name = full_name
        self.__birth_date = birth_date
        self.__contact_phone = contact_phone


    def data_output(self):
        return (
            f"Ф.И.О.: {self.__full_name}\n"
            f"Дата рождения: {self.__birth_date}\n"
            f"Контактный телефон: {self.__contact_phone}"
        )

    def validate_full_name(self, full_name):
        ...
    def validate_birth_date(self, birth_date):
        ...

    def validate_contact_phone(self, contact_phone):
        ...


human = Human("Васечкин Сергей Васильевич", "12.12.2005", "+7(999)680-15-15")
print(human.data_output())