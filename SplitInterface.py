'''
Задание 1
Рассмотрим принцип разделения интерфейсов на следующем примере.
Допустим у нас имеется абстрактный класс Payments и в нем есть три метода:
оплата через электронный кошелек, оплата банковской карточкой и оплата
по QR коду.
class Payments(ABC):
@abstarctmethod
def pay_web_money(self): ...
@abstarctmethod
def pay_сredit_сard(self): ...
@abstarctmethod
def pay_qr_code(self): ...
Выполните разделение интерфейса и создайте два класса-наследника,
которые будут у себя реализовывать различные виды проведения оплат (класс
InternetPaymentService и TerminalPaymentService). При этом
TerminalPaymentService не должен поддерживать проведение оплат через
электронный кошелек.
'''
from abc import ABC, abstractmethod
class Payments(ABC):

    # @abstractmethod
    # # оплата через электронный кошелек
    # def pay_web_money(self, amount: int):
    #     ...

    @abstractmethod
    # оплата банковской карточкой
    def pay_credit_card(self, amount: int):
        ...
    @abstractmethod
    # оплата по QR коду.
    def pay_qr_code(self, amount: int):
        ...

class InternetPaymentService(Payments):

    def pay_web_money(self, amount: int):
        print(f"Оплата на электронный кошелек на сумму {amount} прошла успешно.")

    def pay_credit_card(self, amount: int):
        print(f"Оплата на кредитную карту на сумму {amount} прошла успешно.")

    def pay_qr_code(self, amount: int):
        print(f"Оплата по QR коду на сумму {amount} прошла успешно.")

class TerminalPaymentService(Payments):

    def pay_credit_card(self, amount: int):
        print(f"Оплата на кредитную карту на сумму {amount} прошла успешно.")

    def pay_qr_code(self, amount: int):
        print(f"Оплата по QR коду на сумму {amount} прошла успешно.")


internet_payment = InternetPaymentService()
terminal_payment = TerminalPaymentService()
internet_payment.pay_web_money(890)
internet_payment.pay_qr_code(455)
terminal_payment.pay_credit_card(600)
