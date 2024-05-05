from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birthday = models.DateField()

    birthday_email_sent_year = models.IntegerField(default=None, null=True)  # Stores the year email was sent