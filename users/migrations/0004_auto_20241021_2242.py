# Generated by Django 3.2.25 on 2024-10-21 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_artist_age'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artist',
            new_name='UserProfile',
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
    ]
