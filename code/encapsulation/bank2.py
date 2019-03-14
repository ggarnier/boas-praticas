class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__balance < value:
            raise InsufficientFunds()
        self.__balance -= value

    def report(self):
        print("current balance: ${}".format(self.__balance))


class InsufficientFunds(Exception):
    pass


bank = BankAccount()
bank.__balance += 1000  # AttributeError: 'BankAccount' object has no attribute '__balance'
bank.withdraw(10)  # InsufficientFunds
