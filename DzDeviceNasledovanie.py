'''
Задание 2
Создайте класс Device, который будет содержать информацию об
электронном устройстве. С помощью механизма наследования, реализуйте
класс MobilePhone (содержит информацию об мобильном телефоне). Каждый
из классов должен содержать необходимые для работы методы.
'''
'''
Можно добавить:
бренд,
название, 
год выпуска, 
цвет,
вес,
цена
'''

class Device:
    def __init__(
            self, brand: str,
            model: str,
            release: int,
            color: str,
            weight: float,
            price: float):
        self.__brand = brand
        self.__model = model
        self.__release = release
        self.__color = color
        self.__weight: weight
        self.price = price

class MobilePhone(Device):
    def __init__(self, brand:str, model:str, release:int, color:str, weight:float, battery:int, memory:int, device_type:str, price:float):
        super().__init__(brand, model, release, color, weight, price)
        self.__battery = battery
        self.__memory = memory
        self.__device_type = device_type


mobilephone = MobilePhone("Samsung", "Galaxy A34", 2023, "red", 199.0, 5000, 128, " Смартфон", 21671)
print(mobilephone.__dict__)


