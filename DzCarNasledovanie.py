'''
Задание 1
Создайте класс Car, который будет содержать информацию об
автомобиле. С помощью механизма наследования, реализуйте класс
ElectricCar (содержит информацию об электроавтомобиле). Каждый из
классов должен содержать необходимые для работы методы.
'''

'''
Добавить  информацию об автомобиле:
Марка автомобиля
Модель автомобиля
Год выпуска
Цвет
Номерной знак
объем двигателя

'''

class Car:
    def __init__(
            self, brand: str,
            model: str,
            release: int,
            color: str,
            plate: int,
            engine: float,
            tank: float):
        self.__brand = brand
        self.__model = model
        self.__release = release
        self.__color = color
        self.__plate = plate
        self.__engine = engine
        self.__tank = tank

class ElectricCar(Car):
    def __init__(self, brand, model, release, color, plate, battery_capacity):
        super().__init__(brand, model, release, color, plate)
        self.__battery_capacity = battery_capacity
        self.battery_level = 100

        
        
