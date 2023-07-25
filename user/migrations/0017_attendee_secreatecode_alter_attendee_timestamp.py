# Generated by Django 4.2.2 on 2023-07-24 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0016_alter_attendee_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendee",
            name="secreateCode",
            field=models.CharField(default=True, max_length=12),
        ),
        migrations.AlterField(
            model_name="attendee",
            name="timeStamp",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2023, 7, 24, 16, 22, 40, 644385),
                null=True,
            ),
        ),
    ]
