'''
Задание 2
Рассмотрим принцип открытости-закрытости на примере, созданного в
задании 1 класса по отправке сообщений NotificationService. Допустим нам
необходимо кроме отправки сообщения клиенту по электронной почте
отправлять еще смс сообщения. И мы можем дописать метод send_message
таким образом:
def send_message(type_message: str, message: str, client: Client)
if (type_message == "email"):
# send email
elif (type_message == "sms")
# send sms
Для того чтобы придерживаться принципа открытости-закрытости нам
необходимо спроектировать наш код таким образом, чтобы каждый мог
повторно использовать нашу функцию, просто расширив ее. Поэтому
определим абстрактный класс NotificationService и в нем поместим метод
send_message. Далее создайте класс EmailNotification, который наследуется
от NotificationService и реализует метод отправки сообщений по электронной
почте. Создайте аналогично класс MobileNotification, который будет отвечать
за отправку смс сообщений. Продемонстрируйте работу данного сервиса.
'''

from abc import ABC, abstractmethod
from typing import Optional
class Client:
    def __init__(self, fullname, telephone, email):
        self.fullname = fullname
        self.telephone = telephone
        self.email = email

    def get_details(self):
        return f"Ф.И.О: {self.fullname}, Телефон: {self.telephone}, Email: {self.email}"

class Order:
    def __init__(self, client: Client):
        self.client = client

class CarPrintService:
    def print_order(self, order: Order):
        client_details = order.client.get_details()
        print("Заказ на печать: ")
        print(client_details)

class Car:
    def __init__(self, make: str, model: str, year: int, odometer_reading: int, car_number: str):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
        self.car_number = car_number
        self.is_reserved = False
        self.reservation_start_date = None
        self.reservation_end_date = None

    def reserve_car(self, start_date: str, end_date: str) -> bool:
        if not self.is_reserved:
            self.is_reserved = True
            self.reservation_start_date = start_date
            self.reservation_end_date = end_date
            return True
        else:
            return False

    def cancel_reservation(self, fullname, telephone, email):
        super().__init__(fullname, telephone, email)
        self.is_reserved = False
        self.reservation_start_date = None
        self.reservation_end_date = None

    def get_description(self):
        description = f"{self.make} {self.model} {self.year} с пробегом {self.odometer_reading} км."
        if self.is_reserved:
            description += (f" (Автомобиль {self.car_number} зарезервирован c "
                            f"{self.reservation_start_date} по {self.reservation_end_date} включительно за {client.get_details()})")
        else:
            description += " (Автомобиль доступен для бронирования)"
        return description

class CarInfoService:
    def car_info(self, car: Car):
        car_description = car.get_description()
        return f"Информация об автомобиле: {car_description}"

class NotificationService(ABC):
    @abstractmethod
    def send_message(self, message: str, client: Client):
        ...

class EmailNotification(NotificationService):
    def send_message(self, message: str, client: Client):
        print(f"Отправляем сообщение клиенту по email: {client.fullname}: {message}")

class MobileNotification(NotificationService):
    def send_message(self, message: str, client: Client):
        print(f"Отправляем сообщение клиенту по мобильному телефону: {client.fullname}: {message}")


class RentCarService:
    def __init__(self):
        self.__cars: list[Car] = []

    def search_car(self, car_number:str) -> Optional[Car]:
        for car in self.__cars:
            if car.car_number == car_number:
                return car
        return None

class RentCarService:
    def __init__(self):
        self.__cars: list[Car] = []

    def search_car(self, car_number: str) -> Optional[Car]:
        for car in self.__cars:
            if car.car_number == car_number:
                return car
        return None

    def reservation_car(self, car_number: str, client: Client, start_date: str, end_date: str) -> bool:
        car = self.search_car(car_number)
        if car:
            if not car.is_reserved:
                car.reserve_car(start_date, end_date)
                notification_service = NotificationService()
                message = f"Вы успешно забронировали автомобиль {car.make} {car.model} с {start_date} по {end_date}."
                notification_service.send_message(message, client)
                self.__cars.append(car)  # Добавляем зарезервированную машину в список


                return True
            else:
                # Машина уже зарезервирована, обработка этой ситуации
                print(f"Машина {car.car_number} уже зарезервирована")
                return False
        else:
            # Машина не найдена, обработка этой ситуации
            print(f"Машина с номером {car_number} не найдена")
            return False

    def add_car(self, car: Car) -> None:
        self.__cars.append(car)
        print(f"Автомобиль {car.make} {car.model} успешно добавлен в систему")




client = Client("Петров Иван Иванович", "8(980)680-45-45", "petrov@Yandex.ru")
# Попробуем зарезервировать добавленный автомобиль
order = Order(client)
printer = CarPrintService()
printer.print_order(order)

rent_service = RentCarService()
result = rent_service.reservation_car("B456DE", client, "2024-08-01", "2024-08-15")

# Проверяем информацию об автомобиле после попытки бронирования
car = rent_service.search_car("B456DE")
if car:
    car_info = CarInfoService()
    print(car_info.car_info(car))
else:
    print("Автомобиль не найден")

print("*"*30)
car = rent_service.search_car("A123BC")
if car:
    car_info = CarInfoService()
    print(car_info.car_info(car))
else:
    print("Автомобиль не найден")
if result:
    print("Автомобиль успешно забронирован!")
else:
    print("Не удалось забронировать автомобиль.")


email_message = EmailNotification()
mobile_message = MobileNotification()

# Using the notification services to send messages
email_message.send_message("Вам не удалось забронировать автомобиль", client)
mobile_message.send_message("Вам не удалось забронировать автомобиль", client)