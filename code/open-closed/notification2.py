from abc import abstractmethod


class OrderNotification:
    def __init__(self, order, service):
        self.__order = order
        self.__service = service

    def send(self):
        msg = OrderMessage(self.__order)
        return self.__service.send(msg)


class OrderMessage:
    def __init__(self, order):
        self.__order = order


class NotificationService:
    @abstractmethod
    def send(self, message):
        pass


class Mailer(NotificationService):
    def send(self, message):
        pass


class SMSService(NotificationService):
    def send(self, message):
        pass


# Now I can create new kinds of notification services
# without changing OrderNotification class, including
# fake implementations for tests
class PrintNotification(NotificationService):
    def send(self, message):
        print(message)


class FakeNotification(NotificationService):
    def __init__(self):
        self.__counter = 0

    def send(self, message):
        self.__counter += 1

    def counter(self):
        self.__counter


fake = FakeNotification()
o = OrderNotification(order=Order(), service=fake)
o.send()
print("notification called {} times".format(fake.counter()))
