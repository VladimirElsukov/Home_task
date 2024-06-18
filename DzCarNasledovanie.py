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
            plate: str,
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
    def __init__(self, brand:str, model:str, release:int, color:str, plate:str, battery_capacity:int):
        super().__init__(brand, model, release, color, plate, 0, 0)
        self.__battery_capacity = battery_capacity


        
car = Car("BMW", "X5", 2015, "Red", "М999ОС 77", 2.0, 80)
print(car.__dict__)

electric_car = ElectricCar("TSLA", "Model S/X", 2022, "Red", "А777АА 76", 82)
print(electric_car.__dict__)





