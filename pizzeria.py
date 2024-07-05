'''
Задание 1
Создайте набор классов для эмуляции сценариев работы сервиса для
заказа пиццы в модуле pizzeria.py
Классы должны позволять выполнять следующие сценарии:
1. Отобразить меню пиццерии с рецептами и составом пиццы.
2. Оформить заказ (клиент может заказать более 1 пиццы)
3. Отправка клиенту уведомления о готовности заказа и сроках
доставки
4. Отобразить информацию о заказе с сохранением в файл.
5. Оплатить заказ. Оплата заказа может производиться, как переводом,
так и картой.
6. Необходимо иметь возможность посмотреть количество заказов и
полную выручку за день.
Классы приложения должны быть построены с учетом принципов SOLID.
'''
from abc import ABC, abstractmethod
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Необходимо импортировать pip install twilio если не установлено
from twilio.rest import Client

# 1. Отобразить меню пиццерии с рецептами и составом пиццы.
class PizzeriaMenu:
    def __init__(self):
        self.menu = {
            "Пепперони": "Пепперони, сыр, томатный соус",
            "Маргарита": "Томаты, моцарелла, базилик",
            "Гавайская": "Ветчина, ананас, сыр"
        }

    def menu_display(self):
        menu_output = []
        for pizza_name, structure in self.menu.items():
            menu_output.append(f"Название пиццы => {pizza_name} состав пиццы: {structure}")
        return "\n".join(menu_output)


# 2. Оформить заказ (клиент может заказать более 1 пиццы)
class Order:
    total_orders = 1
    def __init__(self, pizza_menu):
        self.pizza_menu = pizza_menu
        self.cart = []



    def add_pizza_cart(self, pizza):
        if pizza in self.pizza_menu.menu:
            self.cart.append(pizza)
            print(f"Пицца {pizza} добавлена в корзину")
        else:
            print(f"К сожалению пиццы {pizza} нет в меню.")

    def ordering_pizza(self):

        if len(self.cart) == 0:
            print("Корзина пуста. Добавьте пиццу в корзину.")
        else:
            Order.total_orders += 1
            print("Заказ оформлен. Список заказанных пицц: ")
            for pizza in self.cart:
                print(f"-{pizza}")
            ordered_pizzas = list(self.cart)
            self.cart = []
            return ordered_pizzas

    @staticmethod
    def total_order():
        return Order.total_orders


# 3. Отправка клиенту уведомления о готовности заказа и сроках доставки. Функциональность не проверена
class Notification:
    def send_notification(self, order_details, method='email'):
        if method == 'email':
            self.send_email(order_details)
        elif method == 'sms':
            self.send_sms(order_details)

    def send_email(self, order_details):
        # Отправка уведомления по электронной почте
        email_content = f"Уведомление о заказе:\n{order_details}"
        sender_email = 'your_email@example.com'
        receiver_email = 'recipient_email@example.com'
        password = 'your_email_password'

        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Уведомление о заказе'
        message.attach(MIMEText(email_content, 'plain'))

        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print(f"Уведомление отправлено по электронной почте: {order_details}")

    def send_sms(self, order_details):
        # Отправка уведомления по SMS
        account_sid = 'your_account_sid'
        auth_token = 'your_auth_token'
        client = Client(account_sid, auth_token)

        from_number = 'your_twilio_phone_number'
        to_number = 'recipient_phone_number'
        message = client.messages.create(
            body=f"Уведомление о заказе: {order_details}",
            from_=from_number,
            to=to_number
        )

        print(f"Уведомление отправлено по SMS: {order_details}")

# 4. Отобразить информацию о заказе с сохранением в файл.
class InfoSavingFile:
    def save_to_file(self, order_info, file_name='order_info.txt'):
        try:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(f"Order Information:\n{order_info}\n\n")
            print(f"Информация о заказе сохранена в файл: {file_name}")
        except Exception as e:
            print(f"Произошла ошибка при сохранении информации о заказе в файл: {str(e)}")


# 5. Оплатить заказ. Оплата заказа может производиться, как переводом,
# так и картой.
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
        return f"Оплата заказа электронный кошелек на сумму {amount} прошла успешно."

    def pay_credit_card(self, amount: int):
        return f"Оплата заказа по кредитной карте на сумму {amount} прошла успешно."

    def pay_qr_code(self, amount: int):
        return f"Оплата заказа по QR коду на сумму {amount} прошла успешно."

class TerminalPaymentService(Payments):

    def pay_credit_card(self, amount: int):
        return f"Оплата заказа по кредитной карте на сумму {amount} прошла успешно."

    def pay_qr_code(self, amount: int):
        return f"Оплата заказа по QR коду на сумму {amount} прошла успешно."


# 6. Необходимо иметь возможность посмотреть количество заказов и
# полную выручку за день.
class OrderRevenue:
    def __init__(self):
        self.orders = []
        self.total_revenue = 0

    def add_order(self, order_amount):
        self.orders.append(order_amount)
        self.total_revenue += order_amount

    def get_total_orders(self):
        return len(self.orders)

    def get_total_revenue(self):
        return self.total_revenue



print('*'*30)
print('*'*30)
print('*'*30)
pizzeria_menu = PizzeriaMenu()
print(pizzeria_menu.menu_display())
info_saver = InfoSavingFile()
print('*'*30)


# Получаем список заказанных пицц
order = Order(pizzeria_menu)
order.add_pizza_cart("Маргарита")
order.add_pizza_cart("Маргарита")
print('*'*30)


# Создаем первый заказ и добавляем его в корзину, записываем в файл order55.txt
number_order = order.total_order()
print(number_order)
ordered_pizzas = order.ordering_pizza()
# К оплате
cost = 890
# Подтверждаем оплату
internet_payment = InternetPaymentService()
payment = internet_payment.pay_qr_code(cost)

if ordered_pizzas:
    order_info = f"Номер заказа: {number_order}\nСписок пицц: {', '.join(ordered_pizzas)}\nК оплате: {cost}\n{payment}"
    info_saver.save_to_file(order_info, 'order55.txt')
    print("Информация о заказе сохранена.")



print('*'*30)
# Создаем второй заказ и добавляем его в корзину, записываем в файл order55.txt
order = Order(pizzeria_menu)
order.add_pizza_cart("Маргарита")
order.add_pizza_cart("Гавайская")
print('*'*30)
# К оплате
cost = 810
# Подтверждаем оплату
internet_payment = InternetPaymentService()
payment = internet_payment.pay_credit_card(cost)

number_order = order.total_order()
print(number_order)
ordered_pizzas = order.ordering_pizza()
if ordered_pizzas:
    order_info = f"Номер заказа: {number_order}\nСписок пицц: {', '.join(ordered_pizzas)}\nК оплате: {cost}\n{payment}"
    info_saver.save_to_file(order_info, 'order55.txt')
    print(cost)
    print(payment)
    print("Информация о заказе сохранена.")


print('*'*30)
# Создаем третий заказ и добавляем его в корзину, записываем в файл order55.txt, заказы выводятся попорядку
order = Order(pizzeria_menu)
order.add_pizza_cart("Маргарита")
order.add_pizza_cart("Гавайская")
order.add_pizza_cart("Пепперони")
print('*'*30)
# К оплате
cost = 1150
# Подтверждаем оплату
terminal_payment = TerminalPaymentService()
payment = terminal_payment.pay_credit_card(cost)

number_order = order.total_order()
print(number_order)
ordered_pizzas = order.ordering_pizza()
if ordered_pizzas:
    order_info = f"Номер заказа: {number_order}\nСписок пицц: {', '.join(ordered_pizzas)}\nК оплате: {cost}\n{payment}"
    info_saver.save_to_file(order_info, 'order55.txt')
    print("Информация о заказе сохранена.")
    print(cost)
    print(payment)

print('*'*30)


# Cмотрим количество заказов и полную выручку за день.
# Создаем объект для отслеживания заказов и выручки
order_revenue_tracker = OrderRevenue()

# После завершения каждого заказа добавляем информацию о его стоимости в отслеживание выручки, пока вручную, надо создать базу данных
# Здесь предполагается, что каждый заказ имеет свою стоимость, которая сохраняется в списке
costs = [890, 810, 1150]
for cost in costs:
    order_revenue_tracker.add_order(cost)

# После завершения всех заказов выведем информацию о количестве заказов и общей выручке за день
print(f"Общее количество заказов за день: {order_revenue_tracker.get_total_orders()}")
print(f"Общая выручка за день: {order_revenue_tracker.get_total_revenue()}")

