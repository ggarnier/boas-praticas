class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        if self.balance < value:
            raise InsufficientFunds()
        self.balance -= value

    def report(self):
        print("current balance: ${}".format(self.balance))


class InsufficientFunds(Exception):
    pass


bank = BankAccount()
bank.deposit(100)
bank.deposit(20)
bank.withdraw(15)
bank.report()

bank.withdraw(150)  # InsufficientFunds

bank.balance -= 150
bank.report()  # Negative balance
