import unittest
from store3 import Order


class OrderTest(unittest.TestCase):
    def test_finish(self):
        order = Order()
        order.add_item("iphone")
        order.finish(card_number="1234",
                     inventory=FakeInventory(),
                     credit_card=fakeCreditCard(),
                     db=FakeDB(),
                     notification=FakeNotification()
                     )


class FakeInventory:
    def check_items(self):
        pass


class fakeCreditCard:
    def make_payment(self, card_number):
        # Simulate an error in credit card system
        raise Exception("invalid credit card")


class FakeDB:
    def register_order(self):
        pass


class FakeNotification:
    def send_email_to_user(self):
        pass


if __name__ == '__main__':
    unittest.main()
