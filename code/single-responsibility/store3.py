class Order:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    # With dependency injection
    def finish(self, card_number, inventory, credit_card, db, notification):
        inventory.check_items()
        credit_card.make_payment(card_number)
        db.register_order()
        notification.send_email_to_user()
