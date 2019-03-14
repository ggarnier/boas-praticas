import smtplib
from email.message import EmailMessage


class OrderMailer:
    def __init__(self, order):
        self.__order = order

    # This method is responsible for:
    # - Formatting the message fields from an order
    # - Mapping formatted order fields to email fields
    # - Reading a value from a config file
    # - Openning a connection to an SMTP server
    # - Sending an email to the SMTP server
    def send(self):
        msg = EmailMessage()
        msg["Subject"] = "Confirmation for order #{}".format(self.__order.number)
        msg["From"] = "orders@example.com"
        msg["To"] = self.__order.user_email
        text = "Order #{} at {}".format(self.__order.number, self.__order.date)
        text += "Items:"
        for index, item in enumerate(self.__order.items()):
            text += "{}) {} - {}".format(index, item.name, item.price)
        msg.set_content(text)
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
