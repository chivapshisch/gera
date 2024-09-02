# Generated by Django 5.0.6 on 2024-08-16 10:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("index", "0004_names_opisanie"),
    ]

    operations = [
        migrations.CreateModel(
            name="City",
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
                ("town", models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name="names",
            name="adress",
        ),
        migrations.AddField(
            model_name="opisanie",
            name="adress",
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="opisanie",
            name="gorod",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="gorod",
                to="index.city",
            ),
        ),
    ]
