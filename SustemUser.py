'''
Задание 2
Создайте базовый абстрактный класс SystemUser. Опишите следующие
методы:
 Информация о пользователе
 Вход в систему
 Выход из системы
 Сменить пароль
Создайте класс Employee - наследника, класса SystemUser и выполните вход
и выход в системе.
'''

from abc import ABC, abstractmethod

class SystemUser(ABC):
    @abstractmethod
    def user_info(self):
        ...

    @abstractmethod
    def input_system(self):
        ...

    @abstractmethod
    def exit_system(self):
        ...

    @abstractmethod
    def change_password(self):
        ...

class Employee(SystemUser):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__logged_in = False

    def user_info(self):
        return f"Имя пользователя: {self.__username}"

    def input_system(self):
        if not self.__logged_in:
            self.__logged_in = True
            print(f"Пользователь '{self.__username}' вошёл в систему.")
        else:
            print(f"Пользователь '{self.__username}' уже в системе.")

    def exit_system(self):
        if not self.__logged_in:
            self.__logged_in = False
            print(f"Пользователь '{self.__username}' вышёл из системы.")
        else:
            print(f"Пользователь '{self.__username}' не вошёл в систему.")

    def change_password(self, new_password):
        if self.__is_valid_password(new_password):
            self.__password = new_password
            print("Пароль успешно изменён")
        else:
            print("Пароль не соответствует требованиям безопасности")


    def __is_valid_password(self, password):
        if len(password) < 8:
            return False, "Пароль должен содержать не менее 8 символов"

        if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
            return False, "Пароль должен содержать символы в верхнем и нижнем регистрах"

        if not any(c.isdigit() for c in password):
            return False, "Пароль должен содержать хотя бы одну цифру"

        special_characters = r"!@#$%^&*()-_+=/\:;<>,.?|"
        if not any(c in special_characters for c in password):
            return False, "Пароль должен содержать хотя бы один специальный символ"

        return True, password

employee = Employee("Stepan", "12354773")
print(employee.user_info())
employee.input_system()
employee.change_password("77755599")
employee.exit_system()
