'''
Задание 1
Создайте набор классов для эмуляции сценариев работы сервиса для
Написать программу «Автоматизированная информационная система ЖД
вокзала». Система содержит: сведения об отправлении поездов дальнего
следования. Для каждого поезда укажите: номер, время и дату отправления,
станцию отправления и назначения. Реализуйте:
 Вывод расписания о всех поездах за указанную дату;
 Вывод информации о запрашиваемом поезде.
'''
from datetime import datetime

class Train:
    def __init__(self, number, departure_time, arrival_time, departure_station, destination_station, platform):
        self.number = number
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.departure_station = departure_station
        self.destination_station = destination_station
        self.platform = platform

# Расписание поездов
class TrainSchedule:
    def __init__(self):
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def get_train_info(self, train_number):
        train_schedule = {
            "train1": {
                "route": "City A to City B",
                "departure_time": "08:00",
                "arrival_time": "12:00",
                "platform": 3,
                "status": "on time"
            },
            "train12": {
                "route": "City B to City A",
                "departure_time": "07:00",
                "arrival_time": "14:00",
                "platform": 5,
                "status": "on time"
            },
            "train13": {
                "route": "City D to City B",
                "departure_time": "09:00",
                "arrival_time": "15:00",
                "platform": 1,
                "status": "on time"
            }

        }
        if train_number in train_schedule:
            train = train_schedule[train_number]
            return (f"Номер поезда: {train_number} Направление: {train['route']} Время отправления: {train['departure_time']} Время прибытия: {train['arrival_time']} Платформа: {train['platform']} Статус: {train['status']}")
        else:
            return f"Поезд с номером {train_number} не найден в расписании"

    def get_all_trains_for_date(self, date_str):
        date = datetime.strptime(date_str, "%d.%m.%Y").date()
        trains_for_date = [train for train in self.trains if train.departure_time.date() == date]
        if trains_for_date:
            train_info_str = ""
            for train in trains_for_date:
                train_info_str += f"Номер поезда: {train.number} Направление: {train.departure_station} до {train.destination_station} Время отправления: {train.departure_time}, Время прибытия: {train.arrival_time} Платформа: {train.platform} \n"
            return train_info_str
        else:
            return "На указанную дату нет поездов."

schedule = TrainSchedule()


train1 = Train("train1", datetime(2024, 7, 1, 8, 0), datetime(2024, 7, 1, 12, 0), "City A", "City B", "4")
train2 = Train("train2", datetime(2024, 7, 1, 9, 0), datetime(2024, 7, 1, 13, 45), "City C", "City D", "3")
schedule.add_train(train1)
schedule.add_train(train2)


train_info = schedule.get_train_info("train20")
print(train_info)

train_info = schedule.get_train_info("train13")
print(train_info)


print(schedule.get_all_trains_for_date("01.07.2024"))