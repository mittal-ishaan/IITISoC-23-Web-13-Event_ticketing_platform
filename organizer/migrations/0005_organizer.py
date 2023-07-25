# Generated by Django 4.2.2 on 2023-07-09 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0004_alter_ticket_ticketprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizerName', models.CharField(max_length=100)),
                ('organizerContact', models.CharField(max_length=20)),
                ('organizerEmail', models.EmailField(max_length=254)),
                ('organizerAddress', models.CharField(max_length=200)),
                ('organizerBankName', models.CharField(max_length=100)),
                ('organizerBankBranch', models.CharField(max_length=100)),
                ('organizerBankIFSC', models.CharField(max_length=20)),
                ('organizerBankAccount', models.CharField(max_length=20)),
                ('organizerAbout', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.eventdetails')),
            ],
        ),
    ]
