'''
Задание 2
Рассмотрим принцип инверсии зависимостей на следующем примере.
Исправьте код таким образом, чтобы классы и верхних, и нижних уровней
зависели от одних и тех же абстракций, а не от конкретных реализаций.
class AnonymousAuthentication:
def do_authentication(self): ...
class GithubAuthentication:
def do_authentication(self): ...
class FacebookAuthentication:
def do_authentication(self): ...
class Permissions:
def __init__(self, auth: AnonymousAuthentication)
self.auth = auth
def getPermissions(self):
self.auth.do_authentication()

'''

from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def do_authentication(self):
        ...

class AnonymousAuthentication(Authentication):
    def do_authentication(self):
        print("Анонимная аутентификация: дополнительная аутентификация не требуется")

class GithubAuthentication(Authentication):
    def do_authentication(self):
        print("Аутентификация на GitHub: аутентификация с помощью GitHub OAuth")

class FacebookAuthentication(Authentication):
    def do_authentication(self):
        print("Аутентификация на Facebook: аутентификация с помощью Facebook OAuth")

class Permissions:
    def __init__(self, auth: Authentication):
        self.auth = auth

    def get_permissions(self):
        self.auth.do_authentication()
        print("Получение разрешений пользователя на основе аутентификации")

# Создаем экземпляры классов аутентификации
anonymous_auth = AnonymousAuthentication()
github_auth = GithubAuthentication()
facebook_auth = FacebookAuthentication()

# Создаем экземпляры Permissions, используя разные типы аутентификации
anonymous_permissions = Permissions(anonymous_auth)
github_permissions = Permissions(github_auth)
facebook_permissions = Permissions(facebook_auth)

# Вызываем метод get_permissions() для каждого экземпляра Permissions
anonymous_permissions.get_permissions()
github_permissions.get_permissions()
facebook_permissions.get_permissions()