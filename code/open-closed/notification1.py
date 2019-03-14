class OrderNotification:
    def __init__(self, order, kind):
        self.__order = order
        self.__kind = kind

    # If I want to implement a new kind of notification, I'd need to update this class
    def send(self):
        msg = OrderMessage(self.__order)
        if self.__kind == "email":
            return Mailer.send(msg)
        if self.__kind == "sms":
            return SMSService.send(msg)
        raise Exception("not implemented")


class OrderMessage:
    def __init__(self, order):
        self.__order = order


class Mailer:
    def send(self, message):
        pass


class SMSService:
    def send(self, message):
        pass
