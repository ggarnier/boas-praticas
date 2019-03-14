import smtplib
from email.message import EmailMessage


# OrderMessage is responsible for formatting the message fields from an order
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


class OrderMailer:
    def __init__(self, order):
        self.__order = order

    def send(self):
        order_msg = OrderMessage(self.__order)
        msg = EmailMessage()
        msg["Subject"] = order_msg.subject()
        msg["From"] = order_msg.sender()
        msg["To"] = order_msg.recipient()
        msg.set_content(order_msg.body())
        mail_server = "localhost"
        f = open("config")
        for line in f:
            fields = ": ".split(line)
            if fields[0] == "mail_server":
                mail_server = fields[1]
                break
        f.close()
        smtp = smtplib.SMTP(mail_server)
        smtp.send_message(msg)
        smtp.quit()
