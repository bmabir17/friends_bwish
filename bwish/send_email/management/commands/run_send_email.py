from datetime import date
import time
from django.core.management.base import BaseCommand
# from django.db.models import Q
from bwish_api.models import Customer
from bwish import settings
from send_email.send_message import SendMessage
# from send_sms_bot.sms_api import call_sendSMS_api
import logging
send_email_logger = logging.getLogger('send_email')

class Command(BaseCommand):
    help = 'Runs the Email sending Process'

    def handle(self, *args, **options):
        send_email=SendMessage(logger=send_email_logger)
        # print(f"send_sms Val:{settings.send_sms} type: {type(settings.send_sms)}")
        while True:
            if settings.send_email:
                today = date.today()
                current_year = today.year
                print(current_year)
                # Filter for customers with birthdays today
                birthdays_today = Customer.objects.filter(
                    birthday__month=today.month, birthday__day=today.day
                )

                for customer in birthdays_today:
                    if customer.birthday_email_sent_year is None or customer.birthday_email_sent_year < current_year:
                        send_email.send_birthday_email(customer.email, customer.name)
                        customer.birthday_email_sent_year = current_year
                        customer.save()
                print("Sleeping Untill Next Day")
                time.sleep((60))
                # time.sleep((12*60*60))

            else:
                print(f"Process Sleeping for 100 seconds as send_email is {settings.send_sms}")
                time.sleep(100)

    
