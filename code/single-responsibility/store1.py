class Order:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    # Too many responsibilities!
    def finish(self, card_number):
        check_items_in_stock()
        make_payment(card_number)
        save_order()
        send_email_to_user()
