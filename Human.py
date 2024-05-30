'''
Задание 1.
Реализуйте класс «Человек». Необходимо хранить в полях класса: ФИО,
дату рождения, контактный телефон, город, страну, домашний адрес.
Реализуйте конструктор по умолчанию и метод для вывода данных.
'''

class Human:
    def __init__(self, full_name="", birth_date="", contact_phone="", city="", country="", home_address=""):
        self.__full_name = full_name
        self.__birth_date = birth_date
        self.__contact_phone = contact_phone
        self.__city = city
        self.__country = country
        self.__home_address = home_address

    def data_output(self):
        print("Ф.И.О.", self.__full_name)
        print("Дата рождения", self.__birth_date)
        print("Контактный телефон", self.__contact_phone)
        print("Город", self.__city)
        print("Страна", self.__country)
        print("Домашний адрес", self.__home_address)

human = Human("Плюшкин Семён Семёнович", "09.12.1998", "+7(980)565-23-14", "Ярославль", "Россия", "ул.Ленина д.22 кв.1")
human.data_output()