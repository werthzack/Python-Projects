import os
from dotenv import load_dotenv
import smtplib
from twilio.rest import Client

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.mail = input("Input the mail that'll be the sender")
        self.client = os.getenv('SID')
        self.token = os.getenv('AUTH_TOKEN')

    def send_mail(self, target_mail, flight_data, country):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.mail, password="your password here")
            connection.sendmail(
                from_addr=f"Flighty Services <{self.mail}>",
                to_addrs=target_mail,
                msg=f"Subject:Cheap Flight Alert!!!\n\n"
                    f"Low price alert! Only ${flight_data['total_price']} to fly from London to {country} on {flight_data['flight_date']}"
            )

    def send_notification(self, flight_data: dict, country):
        client = Client(self.client, self.token)
        message = client.messages \
            .create(
                body=f"Low price alert! Only ${flight_data['total_price']} to fly from London to {country} on {flight_data['flight_date']}",
                from_="whatsapp: Your twiliio number",
                to="whatsapp: Your target number"
            )
        print(message.status)

