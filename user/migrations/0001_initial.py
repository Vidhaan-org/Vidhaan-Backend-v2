# Generated by Django 4.1.3 on 2022-11-20 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("mobile", models.CharField(max_length=12, unique=True)),
                ("email", models.EmailField(blank=True, max_length=20, null=True)),
                ("password", models.CharField(blank=True, max_length=50, null=True)),
                ("first_name", models.TextField(blank=True, max_length=150, null=True)),
                ("last_name", models.TextField(blank=True, max_length=150, null=True)),
                (
                    "access_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("employee", "employee"),
                            ("official", "official"),
                            ("developer", "developer"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                ("is_staff", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
            ],
            options={
                "verbose_name": "CustomUser",
                "verbose_name_plural": "CustomUser",
            },
        ),
        migrations.CreateModel(
            name="UserPermission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tab_name", models.CharField(max_length=100, unique=True)),
                ("can_operate", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="UserDetails",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("employee", "employee"),
                            ("official", "official"),
                            ("developer", "developer"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Male", "Male"),
                            ("Female", "Female"),
                            ("Others", "Others"),
                        ],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("pin", models.CharField(blank=True, max_length=15, null=True)),
                ("address", models.CharField(blank=True, max_length=200, null=True)),
                ("city", models.CharField(blank=True, max_length=50, null=True)),
                ("district", models.CharField(blank=True, max_length=50, null=True)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("country", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customuser",
            name="permissions",
            field=models.ManyToManyField(blank=True, to="user.userpermission"),
        ),
        migrations.AddField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
