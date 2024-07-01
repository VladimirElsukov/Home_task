'''
Задание 1
Создайте программу, имитирующую многоквартирный дом. Необходимо
иметь классы «Человек», «Квартира», «Дом». Класс «Квартира» содержит
список объектов класса «Человек». Класс «Дом» содержит список объектов
класса «Квартира». Реализуйте:
 Вывод информации о всех жильцах определенной квартиры
 Вывод информации о всех квартирах в определенном доме
'''
class Human:
    def __init__(self, fullname: str, age: int):
        self.__fullname = fullname
        self.__age = age

    def get_fullname(self):
        return self.__fullname

    def get_age(self):
        return self.__age

class Apartment:
    def __init__(self, apartment_number: int, area: float, rooms: int):
        self.__apartment_number = apartment_number
        self.__area = area
        self.__rooms = rooms
        self.__residents = []

    def add_resident(self, resident):
        self.__residents.append(resident)

    def get_apartment_number(self):
        return self.__apartment_number

    def remove_resident(self, resident_name):
        for resident in self.__residents:
            if resident.get_fullname() == resident_name:
                self.__residents.remove(resident)
                return
        print(f"Жилец {resident_name} не найден")

    def list_residents(self):
        result = f"Жильцы в квартире {self.__apartment_number}:\n"
        for resident in self.__residents:
            result += f"- {resident.get_fullname()}, возраст {resident.get_age()}\n"
        return result

class House:
    def __init__(self, address: str):
        self.__address = address
        self.__apartments = []

    def add_apartment(self, apartment):
        self.__apartments.append(apartment)

    def info_residents_apartment(self, apartment_number):
        for apartment in self.__apartments:
            if apartment.get_apartment_number() == apartment_number:
                count_residents = len(apartment.list_residents().split('-')) - 1
                children = sum(
                    1 for resident in apartment.list_residents().split('-') if len(resident.split(',')) > 1 and
                    int(resident.split(',')[1].split()[1]) < 18)
                return f"В квартире {apartment_number} проживает {count_residents} человек, в том числе детей: {children}"
        return f"Квартира {apartment_number} не найдена"

    def list_apartments(self):
        return [apartment.apartment_number for apartment in self.__apartments]

    def info_apartment_house(self):
        result = f"В доме по адресу {self.__address} находятся {len(self.__apartments)} квартир:\n"
        for apartment in self.__apartments:
            result += f"Квартира {apartment.get_apartment_number()} заселена {len(apartment.list_residents().splitlines())} жильцами \n"
        return result

# Создаем квартиры и заселяем их жильцами
apartment1 = Apartment(1, 80.0, 3)
apartment2 = Apartment(2, 65.0, 2)
apartment3 = Apartment(3, 100.0, 4)

apartment1.add_resident(Human("Иванова Елена Ивановна", 28))
apartment1.add_resident(Human("Иванов Дмитрий Иванович", 5))
apartment1.add_resident(Human("Иванова Анна Дмитриевна", 3))

apartment2.add_resident(Human("Петров Михаил Петрович", 27))
apartment2.add_resident(Human("Петрова Екатерина Петровна", 24))

apartment3.add_resident(Human("Сидоров Алексей Сидорович", 45))

# Создаем дом и добавляем в него квартиры
house = House("г.Москва, ул. Примерная, д.1")
house.add_apartment(apartment1)
house.add_apartment(apartment2)
house.add_apartment(apartment3)

# house.apartments.extend([apartment1, apartment2, apartment3])

# Выводим информацию о квартирах в доме
print(house.info_apartment_house())

# Выводим информацию о жильцах в определенной квартире 1
print(house.info_residents_apartment(1))
print(apartment1.list_residents())

# Выводим информацию о жильцах в определенной квартире 2
print(house.info_residents_apartment(2))
print(apartment2.list_residents())


# Выводим информацию о жильцах в определенной квартире 3
print(house.info_residents_apartment(3))
print(apartment3.list_residents())