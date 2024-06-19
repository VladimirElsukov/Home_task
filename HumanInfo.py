'''
Задание 1
Создайте класс Human, который будет содержать информацию о
человеке. С помощью механизма наследования, реализуйте класс Builder
(содержит информацию о строителе), класс Sailor (содержит информацию о
моряке), класс Pilot (содержит информацию о летчике). Каждый из классов
должен содержать необходимые для работы методы.
'''

class Human:
    def __init__(self, full_name:str, birth_date:str, contact_phone:str, city:str, country:str, home_address:str):
        self.__full_name = full_name
        self.__birth_date = birth_date
        self.__contact_phone = contact_phone
        self.__city = city
        self.__country = country
        self.__home_address = home_address

    def data_output(self):
        print("Ф.И.О.:", self.__full_name)
        print("Дата рождения:", self.__birth_date)
        print("Контактный телефон:", self.__contact_phone)
        print("Город:", self.__city)
        print("Страна:", self.__country)
        print("Домашний адрес:", self.__home_address)


class Builder(Human):
    def __init__(self, full_name:str, birth_date:str, contact_phone:str, city:str, country:str, home_address:str, specialization:str, experience:int):
        super().__init__(full_name, birth_date, contact_phone, city, country, home_address)
        self.__specialization = specialization
        self.__experience = experience
    # Переопределение метода data_output
    def data_output(self):
        super().data_output()
        print("Специализация строителя:", self.__specialization)
        print("Стаж работы:", self.__experience, "лет")




human = Human("Плюшкин Семён Семёнович", "09.12.1998", "+7(980)565-23-14", "Ярославль", "Россия", "ул.Ленина д.22 кв.1")
human.data_output()
print("*"*30)
builder = Builder("Васейкин Иван Васильевич", "12.03.84", "+(920)565-35-35", "Ярославль", "Росссия", "ул.Ньютона д.13 кв.13", "Плиточник", 7)
print(builder.__dict__)
print("*"*30)
print(builder.data_output())
