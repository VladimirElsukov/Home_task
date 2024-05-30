'''
Задание 1
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет машины,
цену. Реализуйте конструктор по умолчанию и метод для вывода данных
объекта. Реализуйте методы валидации данных для атрибутов объекта.
Реализуйте доступ к отдельным атрибутам класса через методы объекта
(геттеры и сеттеры), используя декоратор @property и @атрибут.setter.

'''

class Car:
    def __init__(self, model_name: str, year_release: int, manufacturer: str, engine_volume: str, color_car: str, price: float):
        self.__model_name = model_name
        self.__year_release = year_release
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color_car = color_car
        self.__price = price

    def display_info(self):
        return (f"Название модели: {self.__model_name}\n"
               f"Год выпуска: {self.__year_release}\n"
               f"Производитель: {self.__manufacturer}\n"
               f"Объем двигателя: {self.__engine_volume}\n"
               f"Цвет автомобиля: {self.__color_car}\n"
               f"Цена: {self.__price}"
               )

    @property
    def model_name(self):
        return self.__model_name

    @model_name.setter
    def model_name(self, model_name):
        self.__model_name = self.__validate_string(model_name, 'model_name')

    @property
    def year_release(self):
        return self.__year_release

    @year_release.setter
    def year_release(self, year_release):
        self.__year_release = self.__validate_year_release(year_release)

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self.__manufacturer = self.__validate_string(manufacturer, 'manufacturer')

    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, engine_volume):
        self.__engine_volume = self.__validate_float(engine_volume, 'engine_volume')

    @property
    def color_car(self):
        return self.__color_car

    @color_car.setter
    def color_car(self, color_car):
        self.__color_car = self.__validate_string(color_car, 'color_car')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = self.__validate_float(price, 'price')

    def __validate_string(self, value: str, filed_name: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{filed_name} должен быть строкой")
        if not value:
            raise ValueError(f"{filed_name} не может быть пустым")
        if not value[0].isupper():
            raise ValueError(f"Первая буква {filed_name} должна быть заглавной")
        for i in value:
            if not (1040 <= ord(i) <= 1103 or ord(i) == 1025 or ord(i) == 1105 or 65 <= ord(i) <= 122):
                raise ValueError(f"{filed_name} должен содержать только символы кириллицы или латиницы")
        return value.capitalize()

    def __validate_year_release(self, year_release: int) ->int:
        if not isinstance(year_release, int):
            raise TypeError('Параметр year_release должен быть целочисленным')
        if not 1900 <= year_release <= 2024:
            raise ValueError("Неверный год, год выпуска должен быть в диапазоне от 1900 до 2024 включительно.")
        return year_release


    def __validate_float(self, value: float, submitted_parameter: float) ->float:
        if not isinstance(value, float):
            raise TypeError(f"Параметр {submitted_parameter} должен быть дробным.")
        if value < 0:
            raise ValueError(f'{submitted_parameter} не может быть отрицательным')
        return value


car = Car("BMW Х5", 2005, "Немецкий автопроизводитель BMW", "2.0 литра", 'Solid—Alpine white', 4290000)
print(car.display_info())
print("*"*30)
car.model_name = "Audi"
car.year_release = 2004
print(car.display_info())
print("*"*30)
car.price = 4500000.00
car.engine_volume = 2.4
print(car.display_info())





