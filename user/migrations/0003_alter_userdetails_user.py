# Generated by Django 4.1.3 on 2022-11-24 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_alter_customuser_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdetails",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]