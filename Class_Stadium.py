'''
Задание 2.
Реализуйте класс «Стадион». Необходимо хранить в полях класса:
название стадиона, дату открытия, страну, город, вместимость. Реализуйте
конструктор по умолчанию и метод для вывода данных.
'''

class Stadium:
    def __init__(self, stadium="", opening_date="", country="", city="", capacity=""):
        self.__name_stadium = stadium
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def display_info(self):
        print(f"Название стадиона: {self.__name_stadium}")
        print(f"Дата открытия: {self.__opening_date}")
        print(f"Страна: {self.__country}")
        print(f"Город: {self.__city}")
        print(f"Вместимость стадиона {self.__capacity}")

stadium = Stadium("Шинник", "Основан 15 января 1957 года. В 1957—1960 годах носил название 'Химик'", "Россия", "Ярославль", "21 635 посадочных мест (пластиковые сиденья.)")
stadium.display_info()
