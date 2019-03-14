class Inventory:
    def check_items(self):
        pass


class CreditCardService:
    def make_payment(self, card_number):
        pass


class DB:
    def save_order(self):
        pass


class NotificationService:
    def send_email_to_user(self):
        pass


class Order:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def finish(self, card_number):
        Inventory().check_items()
        CreditCardService().make_payment(card_number)
        DB().save_order()
        NotificationService().send_email_to_user()
