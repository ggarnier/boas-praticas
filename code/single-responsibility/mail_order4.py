import smtplib
from email.message import EmailMessage


class OrderMessage:
    def __init__(self, order):
        self.__order = order

    def subject(self):
        return "Confirmation for order #{}".format(self.__order.number)

    def sender(self):
        return "orders@example.com"

    def recipient(self):
        return self.__order.user_email

    def body(self):
        text = "Order #{} at {}".format(self.__order.number, self.__order.date)
        text += "Items:"
        for index, item in enumerate(self.__order.items()):
            text += "{}) {} - {}".format(index, item.name, item.price)
        return text


class OrderMail:
    def __init__(self, order):
        self.__order_msg = OrderMessage(order)

    def msg(self):
        msg = EmailMessage()
        msg["Subject"] = self.__order_msg.subject()
        msg["From"] = self.__order_msg.sender()
        msg["To"] = self.__order_msg.recipient()
        msg.set_content(self.__order_msg.body())
        return msg


# Config is responsible for reading values from a config file
class Config:
    def __init__(self):
        self.__filename = "config"

    def get(self, key, default_value):
        value = default_value
        f = open(self.__filename)
        for line in f:
            fields = ": ".split(line)
            if fields[0] == key:
                value = fields[1]
                break
        f.close()
        return value


class OrderMailer:
    def __init__(self, order):
        self.__order = order

    def send(self):
        order_mail = OrderMail(self.__order)
        mail_server = Config().get(key="mail_server", default_value="localhost")
        smtp = smtplib.SMTP(mail_server)
        smtp.send_message(order_mail.msg())
        smtp.quit()
