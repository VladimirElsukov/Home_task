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