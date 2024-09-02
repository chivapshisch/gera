# Generated by Django 5.0.6 on 2024-08-21 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0013_rename_gorod_opisanie_bbb"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mnenie",
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
                ("ball", models.IntegerField()),
                ("author", models.CharField(max_length=300)),
                (
                    "name",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="ocenka",
                        to="index.names",
                    ),
                ),
            ],
        ),
    ]
