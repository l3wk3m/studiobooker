# Generated by Django 3.2.25 on 2025-01-18 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_studiobooking_booking_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studiobooking',
            old_name='booking_id',
            new_name='id',
        ),
    ]
