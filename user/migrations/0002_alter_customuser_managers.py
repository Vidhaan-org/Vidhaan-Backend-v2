# Generated by Django 4.1.3 on 2022-11-20 10:26

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser", managers=[("objects", user.models.CustomUserManager()),],
        ),
    ]
