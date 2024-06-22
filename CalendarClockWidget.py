'''
Задание 1
Реализуйте принципы множественного наследования на следующем
примере. Для этого реализуйте независимые классы: класс «Clock» и класс
«Calendar». После этого создайте класс «CalendarClockWidget», который
представляет собой комбинацию классов «Clock» и «Calendar».
Создайте экземпляр класса «CalendarClockWidget» и отобразите
текущие дату и время.
Класс «Clock» имитирует тиканье часов. Экземпляр этого класса
содержит время, которое хранится в атрибутах self.hours, self.minutes и
self.seconds. Класс Clock имеет метод tick() который сдвигает текущее время на
1 секунду при каждом вызове.
Класс «Calendar» содержит атрибуты self.day, self.month,
self.year. Вместо метода tick() у него есть метод advance(), который сдвигает
дату на один день при каждом вызове.
Дополнительное задание.
Используя экземпляр класса CalendarClockWidget отобразите дату и
время через одну секунду, используя метод tick().
'''
from datetime import datetime


# Класс «Clock» имитирует тиканье часов.
class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # метод tick() который сдвигает текущее время на 1 секунду при каждом вызове.

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.seconds = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:04d}"



class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # метод advance(), который сдвигает дату на один день при каждом вызове

    def advance(self):
        days_in_month = self.days_in_month(self.month, self.year)
        self.day += 1
        if self.day > days_in_month:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
        print(f"{self.day:02d}.{self.month:02d}.{self.year:02d}")

    def days_in_month(self, month, year):
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
            return 29
        return days_in_month[month]
    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:02d}"

class CalendarClockWidget(Clock, Calendar):
    def __init__(self, year, month, day, hours=0, minutes=0, seconds=0):
        Clock.__init__(self, hours, minutes, seconds)
        Calendar.__init__(self, day, month, year)

    def display_date_time(self):
        print(f"Дата: {self.day:02d}.{self.month:02d}.{self.year:04d}")
        print(f"Время: {self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}")

    def tick(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
                    # обновляем дату
                    self.advance()

widget = CalendarClockWidget(2024, 6, 22, 13, 45, 30)
# Отображаем текущую дату и время
widget.display_date_time()
# Используем метод tick() для перехода через одну секунду
widget.tick()
# Отображаем новую дату и время
widget.display_date_time()
print("*"*30)
widget.tick()
widget.tick()
widget.tick()
widget.tick()
widget.display_date_time()
print("*"*30)
calendar = Calendar(22,6,2024)
# Сдвигаем число при каждом вызове advance()
print(calendar.advance())
print(calendar.advance())
print(calendar.advance())
print(calendar.advance())
print(calendar.advance())
print(calendar.advance())
print(calendar.advance())
print(calendar.advance())
print(calendar.advance())