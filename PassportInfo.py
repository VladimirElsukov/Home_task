'''
Задание 2
Создайте класс Passport (паспорт), который будет содержать
паспортную информацию о гражданине заданной страны. С помощью
механизма наследования, реализуйте класс ForeignPassport (загран.паспорт)
производный от Passport. Напомним, что заграничный паспорт содержит помимо паспортных данных, также данные о визах, номер заграничного
паспорта.
'''
'''
фамилия;
имя;
отчество;
пол;
дата рождения;
место рождения.
серия и номер паспорта;
дата выдачи паспорта
Место выдачи паспорта
....
'''
class Passport:
    def __init__(
            self, last_name:str,
            first_name:str,
            patronymic:str,
            gender:str,
            birth_date:str,
            birthplace:str,
            series_passport:str,
            number_passport:str,
            data_passport:str,
            place_issue_passport:str):

        self.__last_name = last_name
        self.__first_name = first_name
        self.__patronymic = patronymic
        self.__gender = gender
        self.__birth_date = birth_date
        self.__birthplace = birthplace
        self.__series_passport = series_passport
        self.__number_passport = number_passport
        self.__data_passport = data_passport
        self.__place_issue_passport = place_issue_passport

    def information_output(self):
        print("Фамилия:", self.__last_name)
        print("Имя:", self.__first_name)
        print("Отчество:", self.__patronymic)
        print("Пол:", self.__gender)
        print("Дата рождения:", self.__birth_date)
        print("Место рождения:", self.__birthplace)
        print("Серия:", self.__series_passport, "номер:", self.__number_passport, "паспорта.")
        print("Дата выдачи паспорта:", self.__data_passport)
        print("Место выдачи паспорта:", self.__place_issue_passport)


class ForeignPasswort(Passport):
    def __init__(
            self, last_name: str,
            first_name: str,
            patronymic: str,
            gender: str,
            birth_date: str,
            birthplace: str,
            series_passport: str,
            number_passport: str,
            data_passport: str,
            place_issue_passport: str,
            visa_info: str
    ):
        super().__init__(last_name, first_name, patronymic, gender, birth_date, birthplace, series_passport,
                         number_passport, data_passport, place_issue_passport)
        self.__visa_info = visa_info

    def information_output(self):
        super().information_output()
        print("Информация о визе:", self.__visa_info)

passport = Passport("Иванов", "Игорь", "Олегович", "мужской", "23.11.1977", "Москва", "23 45", "123456", "15.08.2020", "Москва, Садовническая ул., 63 с7")
print(passport.information_output())
print("*"*30)
foreignpasswort = ForeignPasswort("Petrov", "Petr", "Petrovich", "man", "20.05.2000", "Yaroslavl", "82", "1323454", "18.05.2021", "Yaroslavl, Sobinova, 48", "Work visa")
print(foreignpasswort.information_output())

