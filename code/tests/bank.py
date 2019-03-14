class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__balance < value:
            raise InsufficientFunds()
        self.__balance -= value

    def balance(self):
        return self.__balance


class InsufficientFunds(Exception):
    pass
