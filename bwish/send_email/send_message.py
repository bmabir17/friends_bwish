from decorators.error_handler import error_handle
import logging

class SendMessage:
    module_name = 'SendMessage'
    def __init__(self, logger):
        self.logger = logger

    # @error_handle(logger='logger')
    # def send_unsent_message(self,unsent_messages):
    
    @error_handle(logger='logger')
    def send_birthday_email(self,email, name):
        # Email content logic here
        subject = "Happy Birthday, {}!".format(name)
        message = "Happy Birthday and many happy returns of the day!"

        self.logger.info(f"Email Sent to {email}")
        print(f"Email Sent to {email}")
        # send_mail(subject, message, 'your_email@example.com', [email])  # Replace with your email