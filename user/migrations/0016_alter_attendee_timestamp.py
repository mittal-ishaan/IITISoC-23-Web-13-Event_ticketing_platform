# Generated by Django 4.2.2 on 2023-07-24 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0015_alter_attendee_timestamp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendee",
            name="timeStamp",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 7, 24, 9, 3, 22, 31554),
                null=True,
            ),
        ),
    ]