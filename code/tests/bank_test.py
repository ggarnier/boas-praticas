import unittest
from bank import BankAccount, InsufficientFunds


class BankAccountTest(unittest.TestCase):
    def test_deposit(self):
        bank = BankAccount()
        bank.deposit(20)
        self.assertEqual(20, bank.balance())

        bank.deposit(15)
        self.assertEqual(35, bank.balance())

    def test_withdraw(self):
        bank = BankAccount()
        bank.deposit(30)
        bank.withdraw(20)
        self.assertEqual(10, bank.balance())

        with self.assertRaises(InsufficientFunds):
            bank.withdraw(50)


if __name__ == '__main__':
    unittest.main()
