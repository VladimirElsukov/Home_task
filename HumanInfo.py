'''
Задание 1
Создайте класс Human, который будет содержать информацию о
человеке. С помощью механизма наследования, реализуйте класс Builder
(содержит информацию о строителе), класс Sailor (содержит информацию о
моряке), класс Pilot (содержит информацию о летчике). Каждый из классов
должен содержать необходимые для работы методы.
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

