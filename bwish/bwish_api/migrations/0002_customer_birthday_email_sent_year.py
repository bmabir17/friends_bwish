# Generated by Django 4.2.11 on 2024-05-05 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bwish_api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="birthday_email_sent_year",
            field=models.IntegerField(default=None, null=True),
        ),
    ]
