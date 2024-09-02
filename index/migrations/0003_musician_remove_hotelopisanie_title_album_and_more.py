# Generated by Django 5.0.6 on 2024-08-15 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0002_rename_name_hotelopisanie_title"),
        ("ocenki", "0002_delete_otzv"),
    ]

    operations = [
        migrations.CreateModel(
            name="Musician",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("instrument", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="hotelopisanie",
            name="title",
        ),
        migrations.CreateModel(
            name="Album",
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
                ("name", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                ("num_stars", models.IntegerField()),
                (
                    "artist",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="album_musician",
                        to="index.musician",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Hotel",
        ),
        migrations.DeleteModel(
            name="HotelOpisanie",
        ),
    ]
