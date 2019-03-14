from datetime import datetime


class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.__transactions = []

    def deposit(self, value):
        self.__transactions.append(DepositTransaction(value))
        self.__balance += value

    def withdraw(self, value):
        if self.__balance < value:
            raise InsufficientFunds()
        self.__transactions.append(WithdrawTransaction(value))
        self.__balance -= value

    def report(self):
        print("current balance: ${}".format(self.__balance))
        print("\nTransactions:")
        for t in self.__transactions:
            print(t.description())


class InsufficientFunds(Exception):
    pass


class Transaction:
    def __init__(self):
        self.__date = datetime.now()

    def date(self):
        return self.__date.strftime("%d/%m/%Y %H:%M:%S")


class DepositTransaction(Transaction):
    def __init__(self, value):
        super().__init__()
        self.__value = value

    def description(self):
        return "[{}] deposit ${}".format(self.date(), self.__value)


class WithdrawTransaction(Transaction):
    def __init__(self, value):
        super().__init__()
        self.__value = value

    def description(self):
        return "[{}] withdraw ${}".format(self.date(), self.__value)


bank = BankAccount()
bank.deposit(50)
bank.withdraw(10)
bank.deposit(200)
bank.withdraw(80)
bank.report()
