'''
Задание 1.
Реализуйте класс «Автомобиль». Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет машины,
цену. Реализуйте конструктор по умолчанию и метод для вывода данных.
'''

class Car:
    def __init__(self, model_name='', year_release=0, manufacturer="", engine_volume="", color_car="", price=0):
        self.__model_name = model_name
        self.__year_release = year_release
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color_car = color_car
        self.__price = price

    def display_info(self):
        print(f"Название модели: {self.__model_name}")
        print(f"Год выпуска: {self.__year_release}")
        print(f"Производитель: {self.__manufacturer}")
        print(f"Объем двигателя: {self.__engine_volume}")
        print(f"Цвет автомобиля: {self.__color_car}")
        print(f"Цена: {self.__price}")


car = Car("BMW X5", 2005, "Немецкий автопроизводитель BMW", "2.0 литра", 'Solid—Alpine white', 4290000)
car.display_info()