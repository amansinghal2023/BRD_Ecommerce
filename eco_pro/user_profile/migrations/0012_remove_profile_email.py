# Generated by Django 4.1.7 on 2023-03-17 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_rename_signup_id_profile_signup_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
